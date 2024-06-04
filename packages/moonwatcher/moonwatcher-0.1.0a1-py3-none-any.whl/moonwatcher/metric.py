from typing import Union

import torch
import numpy as np
import torchmetrics
from sklearn.preprocessing import LabelEncoder

from moonwatcher.utils.data import Task
from moonwatcher.inference.inference import inference
from moonwatcher.dataset.dataset import Slice, MoonwatcherDataset
from moonwatcher.utils.data_storage import (
    load_groundtruths,
    load_predictions,
    do_predictions_exist,
)


def run_inference_if_necessary(model, dataset):
    if not do_predictions_exist(dataset_name=dataset.name, model_name=model.name):
        inference(model=model, dataset=dataset, device=model.device)


def get_original_indices(dataset_or_slice):
    if isinstance(dataset_or_slice, Slice):
        parent_indices = get_original_indices(dataset_or_slice.moonwatcher_dataset)
        return [parent_indices[i] for i in dataset_or_slice.indices]
    elif isinstance(dataset_or_slice, MoonwatcherDataset):
        return list(range(len(dataset_or_slice.dataset)))
    else:
        raise TypeError("Unsupported dataset type")


def load_data(model, dataset_or_slice: Union[MoonwatcherDataset, Slice]):
    relevant_ids = get_original_indices(dataset_or_slice=dataset_or_slice)
    dataset = (
        dataset_or_slice.original_dataset
        if isinstance(dataset_or_slice, Slice)
        else dataset_or_slice
    )

    run_inference_if_necessary(model=model, dataset=dataset)
    groundtruths_loaded = load_groundtruths(dataset_name=dataset.name)
    predictions_loaded = load_predictions(
        dataset_name=dataset.name, model_name=model.name
    )

    return relevant_ids, dataset, groundtruths_loaded, predictions_loaded


def calculate_metric_internal(
    model,
    relevant_ids,
    dataset,
    groundtruths_loaded,
    predictions_loaded,
    metric: str,
    metric_parameters=None,
):
    if metric_parameters is None:
        metric_parameters = {}

    metric_type = model.task
    metric_function = _METRIC_FUNCTIONS[metric]

    if metric_type == Task.CLASSIFICATION.value:
        try:
            groundtruths = np.array(
                [groundtruths_loaded[i].labels.item() for i in relevant_ids],
                dtype=np.int32,
            )
        except Exception as e:
            raise Exception(
                f"Groundtruths could not be loaded. Dataset output transform should return labels as a 1-dimensional int Tensor of shape (1): {e}"
            )

        try:
            predictions = np.array(
                [predictions_loaded[i].labels.item() for i in relevant_ids],
                dtype=np.int32,
            )
        except Exception as e:
            raise Exception(
                f"Predictions could not be loaded. Model output transform should return labels as an int Tensor of shape (num_boxes): {e}"
            )

        if not groundtruths.size or not predictions.size:
            raise ValueError(
                "Ground truths and/or predictions are empty! Ensure your dataset or slice contains data and has been properly processed."
            )

        try:
            num_classes = len(dataset.label_to_name)
            if num_classes == 2:
                task_type = "binary"
            else:
                task_type = "multiclass"
                label_encoder = LabelEncoder()
                label_encoder.fit(list(dataset.label_to_name.keys()))
                groundtruths = label_encoder.transform(groundtruths.ravel())
                predictions = label_encoder.transform(predictions.ravel())

            groundtruths = torch.tensor(groundtruths).flatten()
            predictions = torch.tensor(predictions).flatten()

            if "average" not in metric_parameters:
                metric_parameters["average"] = "macro"

            metric_value = metric_function(
                predictions,
                groundtruths,
                task=task_type,
                num_classes=num_classes,
                **metric_parameters,
            )

        except Exception as e:
            raise Exception(
                f"Error occured during metric computation. Check if dataset output_transform and model output_transform return the required format: {e}"
            )
    elif metric_type == Task.DETECTION.value:
        try:
            groundtruths = [groundtruths_loaded[i].to_dict() for i in relevant_ids]
            predictions = [predictions_loaded[i].to_dict() for i in relevant_ids]

            groundtruths, predictions = zip(
                *[
                    (gt, pred)
                    for gt, pred in zip(groundtruths, predictions)
                    if gt["boxes"].numel() > 0 and pred["boxes"].numel() > 0
                ]
            )

            if not groundtruths or not predictions:
                raise ValueError(
                    "Ground truths and/or predictions are empty! Ensure your dataset or slice contains data and has been properly processed."
                )

            for gt in groundtruths:
                if "boxes" not in gt or len(gt["boxes"]) == 0:
                    raise ValueError(f"Groundtruth boxes are empty for an entry: {gt}")
            for pred in predictions:
                if "boxes" not in pred or len(pred["boxes"]) == 0:
                    raise ValueError(f"Prediction boxes are empty for an entry: {pred}")

            if metric in ["mAP", "mAP_small", "mAP_medium", "mAP_large"]:
                metric_parameters["iou_type"] = "bbox"
                metric_function = metric_function(**metric_parameters)
                metric_function.update(predictions, groundtruths)
                metric_value = metric_function.compute()
                metric_value = metric_value[_METRIC_KEYS[metric]]
            else:
                metric_value = metric_function(predictions, groundtruths)
                metric_value = metric_value[_METRIC_KEYS[metric]]

        except Exception as e:
            raise Exception(
                f"Error occured during metric computation. Check if dataset output_transform and model output_transform return the required format: {e}"
            )

    return round(metric_value.item(), 5)


def calculate_metric(
    model,
    dataset_or_slice: Union[MoonwatcherDataset, Slice],
    metric: str,
    metric_parameters=None,
):
    relevant_ids, dataset, groundtruths_loaded, predictions_loaded = load_data(
        model, dataset_or_slice
    )
    return calculate_metric_internal(
        model,
        relevant_ids,
        dataset,
        groundtruths_loaded,
        predictions_loaded,
        metric,
        metric_parameters,
    )


_METRIC_FUNCTIONS = {
    "Accuracy": torchmetrics.functional.accuracy,
    "Precision": torchmetrics.functional.precision,
    "Recall": torchmetrics.functional.recall,
    "F1_Score": torchmetrics.functional.f1_score,
    "HammingDistance": torchmetrics.functional.hamming_distance,
    "mAP": torchmetrics.detection.MeanAveragePrecision,
    "mAP_small": torchmetrics.detection.MeanAveragePrecision,
    "mAP_medium": torchmetrics.detection.MeanAveragePrecision,
    "mAP_large": torchmetrics.detection.MeanAveragePrecision,
    "CompleteIntersectionOverUnion": torchmetrics.detection.CompleteIntersectionOverUnion(),
    "DistanceIntersectionOverUnion": torchmetrics.detection.DistanceIntersectionOverUnion(),
    "GeneralizedIntersectionOverUnion": torchmetrics.detection.GeneralizedIntersectionOverUnion(),
    "IntersectionOverUnion": torchmetrics.detection.IntersectionOverUnion(),
}


_METRIC_KEYS = {
    "mAP": "map",
    "mAP_small": "map_small",
    "mAP_medium": "map_medium",
    "mAP_large": "map_large",
    "CompleteIntersectionOverUnion": "ciou",
    "DistanceIntersectionOverUnion": "diou",
    "GeneralizedIntersectionOverUnion": "giou",
    "IntersectionOverUnion": "iou",
}
