import abc
import typing

import numpy as np
from sklearn.metrics import f1_score

import merci.exceptions
import merci.measures
import merci.types


class ModelEvaluator(abc.ABC):
    """
    Base class for model evaluators.
    Validates the dataset and provides a common interface for evaluation.
    """

    def __init__(
        self,
        model: merci.types.Classifier | merci.types.ClassifierProba,
        train_dataset: merci.types.Dataset,
        test_dataset: merci.types.Dataset,
    ) -> None:
        """
        Initialize the model evaluator.

        :param model: Classification model to evaluate
        :param train_dataset: A tuple containing input and target data for training
        :param test_dataset: A tuple containing input and target data for testing
        """
        self.validate_dataset(train_dataset)
        self.validate_dataset(test_dataset)

        self.model = model
        self.train_dataset = train_dataset
        self.test_dataset = test_dataset

    def validate_dataset(self, dataset: merci.types.Dataset) -> None:
        """
        Validate the input dataset.

        :param dataset: A tuple containing input and target data
        :raises merci.exceptions.InvalidDataset: If input and target data have different lengths
        :raises merci.exceptions.InvalidDataset: If input data is empty
        """

        X, y = dataset
        if len(X) != len(y):
            raise merci.exceptions.InvalidDataset(
                "Input and target data must have the same length"
            )
        if not len(X):
            raise merci.exceptions.InvalidDataset("Input data must not be empty")

        all_target_numeric = all(isinstance(yi, np.number) for yi in y)
        all_target_distribution = all(
            isinstance(yi, np.ndarray) and np.isclose(np.sum(yi), 1) and np.all(yi >= 0)
            for yi in y
        )
        if not (all_target_numeric or all_target_distribution):
            raise merci.exceptions.InvalidDataset(
                "Target data must be numeric or a probability distribution"
            )

    @abc.abstractmethod
    def evaluate(self) -> float:
        """
        Evaluate the model using the provided dataset.
        """
        pass


class TransductiveEvaluator(ModelEvaluator):
    """
    Transductive model evaluator. Evaluates the reliability of a probabilistic
    classifier (a classifier that returns a probability distribution) using a
    transductive framework.

    Key Idea: Compare the model's behavior when an example is classified in isolation
    (inductive step) versus when it is added to the training set and then classified
    (transductive step). A larger difference suggests lower reliability.

    The reliabilities of individual predictions are aggregated, averaged, and then
    finally shifted to the [0,1] range, where 1 denotes perfect reliability.

    Implementation is based on the paper:
    @InProceedings{10.1007/3-540-36755-1_19,
        author="Kukar, Matja{\v{z}}
        and Kononenko, Igor",
        editor="Elomaa, Tapio
        and Mannila, Heikki
        and Toivonen, Hannu",
        title="Reliable Classifications with Machine Learning",
        booktitle="Machine Learning: ECML 2002",
        year="2002",
        publisher="Springer Berlin Heidelberg",
        address="Berlin, Heidelberg",
        pages="219--231",
        abstract="In the past decades Machine Learning algorithms have been successfully used in numerous classification problems. While they usually significantly outperform domain experts (in terms of classification accuracy or otherwise), they are mostly not being used in practice. A plausible reason for this is that it is difficult to obtain an unbiased estimation of a single classification's reliability. In the paper we propose a general transductive method for estimation of classification's reliability on single examples that is independent of the applied Machine Learning algorithm. We compare our method with existing approaches and discuss its advantages. We perform extensive testing on 14 domains and 6 Machine Learning algorithms and show that our approach can frequently yield more than 100{\%} improvement in reliability estimation performance.",
        isbn="978-3-540-36755-0"
    }
    """

    Merger = typing.Callable[
        [merci.types.Dataset, merci.types.Dataset], merci.types.Dataset
    ]

    @staticmethod
    def numpy_merger(
        train: merci.types.Dataset, test: merci.types.Dataset
    ) -> merci.types.Dataset:
        """
        Merge the train and test datasets by concatenating them.

        :param train: A tuple containing input and target data for training
        :param test: A tuple containing input and target data for testing
        :return: A tuple containing the merged input and target data
        """
        return (
            np.concatenate([train[0], test[0]]),
            np.concatenate([train[1], test[1]]),
        )

    @staticmethod
    def list_merger(
        train: merci.types.Dataset, test: merci.types.Dataset
    ) -> merci.types.Dataset:
        """
        Merge the train and test datasets by concatenating them.

        :param train: A tuple containing input and target data for training
        :param test: A tuple containing input and target data for testing
        :return: A tuple containing the merged input and target data
        """
        return (
            train[0] + test[0],
            train[1] + test[1],
        )

    def __init__(
        self,
        model: merci.types.ClassifierProba,
        train_dataset: merci.types.Dataset,
        test_dataset: merci.types.Dataset,
        merger: Merger = numpy_merger,
    ) -> None:
        """
        :param model: Classification model to evaluate
        :param train_dataset: A tuple containing input and target data for training
        :param test_dataset: A tuple containing input and target data for testing
        :param merger: A function to merge the train and test datasets, defaults to concatenation
        """
        super().__init__(model, train_dataset, test_dataset)
        self.merger = merger

    def evaluate(self) -> float:
        """
        Evaluate the model using the provided dataset.

        :return: The reliability estimation of the model on the dataset
        """
        # === inductive step ===
        X_train, y_train = self.train_dataset
        X_test, _ = self.test_dataset

        y_test_pred = self.model.predict_proba(X_test)
        y_test_labels = np.argmax(y_test_pred, axis=1)
        merged_dataset = self.merger((X_train, y_train), (X_test, y_test_labels))
        self.model.fit(*merged_dataset)

        # === transductive step ===
        y_transductive_pred = self.model.predict_proba(X_test)
        score = merci.measures.transductive_reliability_estimation(
            y_test_pred, y_transductive_pred
        )
        return score


class DistributionShiftEvaluator(ModelEvaluator):
    """
    Evaluate robustness of the model typ to distribution shift with automatically
    generated shifts of the training data.
    """

    def __init__(
        self,
        model: merci.types.Classifier,
        train_dataset: merci.types.Dataset,
        test_dataset: merci.types.Dataset,
        thresholds: list[float] = None,
        seed: int = 0,
    ) -> None:
        """
        :param model: Classification model to evaluate
        :param train_dataset: A tuple containing input and target data for training
        :param test_dataset: A tuple containing input and target data for testing
        :param thresholds: The thresholds to use for the distribution shift, defaults to [0.75, 0.5, 0.25, 0.1]
        :param seed: The random seed to use for reproducibility, defaults to 0
        """
        super().__init__(model, train_dataset, test_dataset)
        self.thresholds = thresholds
        if self.thresholds is None:
            self.thresholds = [0.75, 0.5, 0.25, 0.1]
        self.rng = np.random.default_rng(seed)

    def evaluate(self) -> float:
        """
        Evaluate the model using the provided dataset.

        :return: The distribution shift robustness estimation of the model on the dataset
        """
        x_train, y_train = self.train_dataset
        x_test, y_test = self.test_dataset
        scores = []
        class0 = np.where(y_train == 0)[0]
        class1 = np.where(y_train == 1)[0]
        for cls, other_cls in zip([class0, class1], [class1, class0]):
            for thr in self.thresholds:
                reduced = self.rng.choice(cls, np.floor(len(cls) * thr).astype(int))
                x_train_shifted = np.append(
                    x_train[other_cls], x_train[reduced], axis=0
                )
                y_train_shifted = np.append(
                    y_train[other_cls], y_train[reduced], axis=0
                )
                self.model.fit(x_train_shifted, y_train_shifted)
                score = f1_score(y_test, self.model.predict(x_test), zero_division=0)
                scores.append(score)
        return np.mean(scores)


class FairnessEvaluator(ModelEvaluator):
    """
    Fairness model evaluator.
    """

    def __init__(
        self,
        model: merci.types.Classifier,
        train_dataset: merci.types.Dataset,
        test_dataset: merci.types.Dataset,
        sensitive_attribute_idx: int = 0,
    ) -> None:
        """
        Initialize the fairness model evaluator.

        :param model: Classification model to evaluate
        :param train_dataset: A tuple containing input and target data for training
        :param test_dataset: A tuple containing input and target data for testing
        :sensitive_attribute_idx: Index of the sensitive attribute in the input data
        """
        super().__init__(model, train_dataset, test_dataset)
        self.validate_sensitive_attribute(
            np.concatenate((train_dataset[0], test_dataset[0]), axis=0),
            sensitive_attribute_idx,
        )
        self.sensitive_attribute_idx = sensitive_attribute_idx

    def validate_sensitive_attribute(
        self, dataset: merci.types.Dataset, sensitive_attribute_idx: int
    ) -> None:

        if sensitive_attribute_idx >= dataset.shape[1]:
            raise merci.exceptions.SensitiveAttributeException(
                f"Invalid sensitive attribute index: {sensitive_attribute_idx}"
            )
        if not np.all(
            np.logical_or(
                dataset[:, sensitive_attribute_idx] == 0,
                dataset[:, sensitive_attribute_idx] == 1,
            )
        ):
            raise merci.exceptions.SensitiveAttributeException(
                "Sensitive attribute must be binary"
            )

    def predictive_parity(self) -> float:
        """
        Calculate the predictive parity fairness measure.

        :return: Absolute difference in positive predictive value (PPV) between protected groups.
        """
        # P(Y = 1|d = 1, G = m) = P(Y = 1|d = 1, G = f)
        return merci.measures.fairness_measure_parametrized(
            self.test_dataset,
            self.model,
            1,  # predicted class
            1,  # true class
            self.sensitive_attribute_idx,
        )

    def predictive_equality(self) -> float:
        """
        Calculate the predictive equality fairness measure.

        :return: Predictive equality difference.
        """
        # P(d = 1|Y = 0, G = m) = P(d = 1|Y = 0, G = f)
        return merci.measures.fairness_measure_parametrized(
            self.test_dataset,
            self.model,
            1,  # predicted class
            0,  # true class
            self.sensitive_attribute_idx,
            "true",  # denominator
        )

    def equal_opportunity(self) -> float:
        """
        Calculate the equal opportunity fairness measure.

        :return: Equal opportunity difference.
        """
        # P(d = 0|Y = 1, G = m) = P(d = 0|Y = 1, G = f)
        return merci.measures.fairness_measure_parametrized(
            self.test_dataset,
            self.model,
            0,  # predicted class
            1,  # true class
            self.sensitive_attribute_idx,
            "true",  # denominator
        )

    def equalized_odds(self) -> float:
        """
        Calculate the equalized odds fairness measure.

        :return: Equalized odds difference.
        """
        # P(d = 1|Y = i, G = m) = P(d = 1|Y = i, G = f), i in {0, 1}
        return (self.equal_opportunity() + self.predictive_equality()) / 2

    def conditional_use_accuracy(self) -> float:
        """
        Calculate the conditional use accuracy fairness measure.

        :return: Conditional use accuracy difference.
        """
        # (P(Y = 1|d = 1, G = m) = P(Y = 1|d = 1, G = f )) ∧ (P(Y = 0|d = 0, G = m) = P(Y = 0|d = 0, G = f))
        ppv = self.predictive_parity()
        npv = merci.measures.fairness_measure_parametrized(
            self.test_dataset,
            self.model,
            0,  # predicted class
            0,  # true class
            self.sensitive_attribute_idx,
        )
        return (ppv + npv) / 2

    def overall_accuracy_equality(self) -> float:
        """
        Calculate the overall accuracy equality fairness measure.

        :return: Overall accuracy equality difference.
        """
        # P(d = Y , G = m) = P(d = Y , G = f )
        X_test, y_test = self.test_dataset
        sensitive_attr = X_test[:, self.sensitive_attribute_idx]
        y_pred = self.model.predict(X_test)

        values = []
        for group in [0, 1]:
            group_indices = np.where(sensitive_attr == group)
            accuracy = np.mean(y_pred[group_indices] == y_test[group_indices])
            values.append(accuracy)
        return abs(values[0] - values[1])

    def treatment_equality(self) -> float:
        """
        Calculate the treatment equality fairness measure.

        :return: Treatment equality difference.
        """
        # FN/FP (G = m) = FN/FP (G = f)
        X_test, y_test = self.test_dataset
        sensitive_attr = X_test[:, self.sensitive_attribute_idx]
        y_pred = self.model.predict(X_test)

        values = []
        for group in [0, 1]:
            group_indices = np.where(sensitive_attr == group)
            fn = np.sum((y_pred[group_indices] == 0) & (y_test[group_indices] == 1))
            fp = np.sum((y_pred[group_indices] == 1) & (y_test[group_indices] == 0))
            values.append(fn / fp if fp != 0 else 0)
        return abs(values[0] - values[1])

    def evaluate(self, measure: str = "predictive_parity") -> float:
        """
        Evaluate model's fairness using the provided dataset.

        :param measure: The fairness measure to evaluate; supported measures are
        'predictive_parity', 'predictive_equality', 'equal_opportunity', 'equalized_odds',
        'conditional_use_accuracy', 'overall_accuracy_equality', and 'treatment_equality'.

        :return: Fairness measure based on the provided measure type.
        """
        fairness_measures = {
            "predictive_parity": self.predictive_parity,
            "predictive_equality": self.predictive_equality,
            "equal_opportunity": self.equal_opportunity,
            "equalized_odds": self.equalized_odds,
            "conditional_use_accuracy": self.conditional_use_accuracy,
            "overall_accuracy_equality": self.overall_accuracy_equality,
            "treatment_equality": self.treatment_equality,
        }

        calculation = fairness_measures.get(measure)
        if calculation is None:
            raise merci.exceptions.InvalidFairnessMeasure(
                f"Invalid fairness measure: {measure}. Supported measures are {list(fairness_measures.keys())}"
            )

        X_test, y_test = self.test_dataset
        sensitive_attr = X_test[:, self.sensitive_attribute_idx]
        return calculation()


class CalibrationEvaluator(ModelEvaluator):
    """
    Evaluate expected calibration error
    """

    def __init__(
        self,
        model: merci.types.ClassifierProba,
        train_dataset: merci.types.Dataset,
        test_dataset: merci.types.Dataset,
    ) -> None:
        """
        Initialize the transductive model evaluator.

        :param model: Classification model to evaluate
        :param train_dataset: A tuple containing input and target data for training
        :param test_dataset: A tuple containing input and target data for testing
        """
        super().__init__(model, train_dataset, test_dataset)

    def evaluate(self) -> float:
        """
        Evaluate the model using the provided dataset.

        :return: The expected calibration error of the model on the dataset
        """
        x_test, y_test = self.test_dataset
        preds = self.model.predict_proba(x_test)[:, 1]
        ece = merci.measures.expected_calibration_error(y_test, preds)
        return ece
