import numpy as np
import pandas as pd

import merci.exceptions
import merci.types


def to_probability_distribution(y: np.ndarray) -> np.ndarray:
    """
    Convert the target data to a probability distribution.

    :param y: array of target data (labels or probability distribution)
    :return: probability distribution
    """
    if len(y.shape) == 1:
        y = y.reshape(-1, 1)
    if len(y[0].shape) < 2:
        num_targets = max(np.max(y), 1) + 1
        y = np.eye(num_targets)[y.flatten()]
    return y


def kl_divergence(p: np.ndarray, q: np.ndarray) -> np.ndarray:
    if p.shape != q.shape:
        raise merci.exceptions.MerciException(
            "Input and target data must have the same length"
        )

    kl_divergence = np.where((p != 0) & (q != 0), p * np.log(p / q), 0).sum(axis=1)
    return kl_divergence


def symmetrict_kl_divergence(p: np.ndarray, q: np.ndarray) -> np.ndarray:
    return (kl_divergence(p, q) + kl_divergence(q, p)) / 2


EPSILON = 1e-15


def cross_entropy(p: np.ndarray, q: np.ndarray) -> np.ndarray:
    if p.shape != q.shape:
        raise merci.exceptions.MerciException(
            "Input and target data must have the same length"
        )

    return -np.sum(p * np.log(q + EPSILON), axis=1)


def transductive_reliability_estimation(p: np.ndarray, q: np.ndarray) -> float:
    """
    Computes reliability of a model by comparing the two probability distributions.
    Uses the cross entropy to compute the difference.
    The reliability is then computed as a function of the cross entropy to remap it to [0, 1] range,
    where 0 means the model is not reliable and 1 means the model is reliable.

    :param p: predictions of the model
    :param q: predictions of the model to compare with
    :return: reliability of the model
    """
    ce = cross_entropy(p, q).mean()
    return np.round(2 / (1 + np.exp(ce)), 5)


def expected_calibration_error(y_test: np.ndarray, y_pred: np.ndarray) -> float:
    """
    Computes Expected Calibration Error (ECE), which is a weighted average of the
    difference between the mean predicted value and the fraction of positives in M bins.
    :param y_test: y values of test set
    :param y_pred: predicted probabilities
    :return: ECE
    """
    df = pd.DataFrame({"target": y_test, "proba": y_pred, "bin": np.nan})
    lim_inf = np.linspace(0, 0.9, 10)
    for idx, lim in enumerate(lim_inf):
        df.loc[df["proba"] >= lim, "bin"] = idx

    bin_groups = pd.concat([df.groupby("bin").mean(), df["bin"].value_counts()], axis=1)
    bin_groups["ece"] = (bin_groups["target"] - bin_groups["proba"]).abs() * (
        bin_groups.index / df.shape[0]
    )
    return bin_groups["ece"].sum()


def fairness_measure_parametrized(
    test_dataset: np.ndarray,
    model: merci.types.Classifier,
    pred_class: int = 0,
    true_class: int = 0,
    sensitive_attribute_idx: int = 0,
    denominator: str = "predicted",
) -> float:
    """
    Calculate the fairness measure for a given model, dataset, and parameters.

    :param test_dataset: A tuple containing input and target data for testing
    :param model: Classification model to evaluate
    :param pred_class: The class predicted by the model
    :param true_class: The true class
    :param sensitive_attribute_idx: The sensitive attribute index
    :param denominator: The denominator for the fairness measure calculation
    :return: The fairness measure based on the provided parameters
    """
    X_test, y_test = test_dataset
    sensitive_attr = X_test[:, sensitive_attribute_idx]
    y_pred = model.predict(X_test)

    values = []
    for group in [0, 1]:
        group_indices = sensitive_attr == group

        y_true_group = y_test[group_indices]
        y_pred_group = y_pred[group_indices]
        joint_cases = np.sum(
            (y_pred_group == pred_class) & (y_true_group == true_class)
        )
        total_predicted_class = np.sum(y_pred_group == pred_class)
        total_true_class = np.sum(y_true_group == true_class)

        if denominator == "predicted":
            val = (
                joint_cases / total_predicted_class if total_predicted_class != 0 else 0
            )
        else:
            val = joint_cases / total_true_class if total_true_class != 0 else 0
        values.append(val)

    return abs(values[0] - values[1])
