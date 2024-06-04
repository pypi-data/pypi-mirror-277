"""Metric classes for computing accuracy scores."""

from cyclops.evaluate.metrics.experimental._stat_scores import (
    _AbstractBinaryStatScores,
    _AbstractMulticlassStatScores,
    _AbstractMultilabelStatScores,
)
from cyclops.evaluate.metrics.experimental.functional.accuracy import (
    _accuracy_compute,
    _binary_accuracy_compute,
)
from cyclops.evaluate.metrics.experimental.utils.types import Array


class BinaryAccuracy(_AbstractBinaryStatScores, registry_key="binary_accuracy"):
    """A measure of how well a binary classifier correctly identifies a condition.

    Parameters
    ----------
    threshold : float, default=0.5
        Threshold for converting probabilities into binary values.
    ignore_index : int, optional
        Values in the target array to ignore when computing the metric.
    **kwargs
        Additional keyword arguments common to all metrics.

    Examples
    --------
    >>> from cyclops.evaluate.metrics.experimental import BinaryAccuracy
    >>> import numpy.array_api as anp
    >>> target = anp.asarray([0, 1, 0, 1])
    >>> preds = anp.asarray([0, 1, 1, 1])
    >>> metric = BinaryAccuracy()
    >>> metric(target, preds)
    Array(0.75, dtype=float32)
    >>> metric.reset()
    >>> target = [[0, 1, 0, 1], [1, 0, 1, 0]]
    >>> preds = [[0, 1, 1, 1], [1, 0, 1, 0]]
    >>> for t, p in zip(target, preds):
    ...     metric.update(anp.asarray(t), anp.asarray(p))
    >>> metric.compute()
    Array(0.875, dtype=float32)

    """

    name: str = "Accuracy Score"

    def _compute_metric(self) -> Array:
        """Compute the accuracy score."""
        tn, fp, fn, tp = self._final_state()
        return _binary_accuracy_compute(tn=tn, fp=fp, fn=fn, tp=tp)


class MulticlassAccuracy(
    _AbstractMulticlassStatScores,
    registry_key="multiclass_accuracy",
):
    """The fraction of correctly classified samples.

    Parameters
    ----------
    num_classes : int
        The number of classes in the classification task.
    top_k : int, default=1
        The number of highest probability or logit score predictions to consider
        when computing the accuracy score. By default, only the top prediction is
        considered. This parameter is ignored if `preds` contains integer values.
    average : {'micro', 'macro', 'weighted', 'none'}, optional, default='micro'
        Specifies the type of averaging to apply to the accuracy scores. Should be one
        of the following:
        - `'micro'`: Compute the accuracy score globally by considering all predictions
            and all targets.
        - `'macro'`: Compute the accuracy score for each class individually and then
            take the unweighted mean of the accuracy scores.
        - `'weighted'`: Compute the accuracy score for each class individually and then
            take the mean of the accuracy scores weighted by the support (the number of
            true positives + the number of false negatives) for each class.
        - `'none'` or `None`: Compute the accuracy score for each class individually
            and return the scores as an array.
    ignore_index : int or tuple of int, optional, default=None
        Specifies a target class that is ignored when computing the accuracy score.
        Ignoring a target class means that the corresponding predictions do not
        contribute to the accuracy score.

    Examples
    --------
    >>> from cyclops.evaluate.metrics.experimental import MulticlassAccuracy
    >>> import numpy.array_api as anp
    >>> target = anp.asarray([0, 1, 2, 2, 2])
    >>> preds = anp.asarray([0, 0, 2, 2, 1])
    >>> metric = MulticlassAccuracy(num_classes=3)
    >>> metric(target, preds)
    Array(0.6, dtype=float32)
    >>> metric.reset()
    >>> target = [[0, 1, 2], [2, 1, 0]]
    >>> preds = [
    ...     [[0.05, 0.95, 0], [0.1, 0.8, 0.1], [0.2, 0.6, 0.2]],
    ...     [[0.1, 0.8, 0.1], [0.05, 0.95, 0], [0.2, 0.6, 0.2]],
    ... ]
    >>> for t, p in zip(target, preds):
    ...     metric.update(anp.asarray(t), anp.asarray(p))
    >>> metric.compute()
    Array(0.33333334, dtype=float32)

    """

    name: str = "Accuracy Score"

    def _compute_metric(self) -> Array:
        """Compute the accuracy score."""
        tn, fp, fn, tp = self._final_state()
        return _accuracy_compute(
            tp=tp,
            fp=fp,
            tn=tn,
            fn=fn,
            is_multilabel=False,
            average=self.average,
        )


class MultilabelAccuracy(
    _AbstractMultilabelStatScores,
    registry_key="multilabel_accuracy",
):
    """The fraction of correctly classified samples.

    Parameters
    ----------
    num_labels : int
        The number of labels in the classification task.
    threshold : float, optional, default=0.5
        The threshold used to convert probabilities to binary values.
    top_k : int, optional, default=1
        The number of highest probability predictions to assign the value `1`
        (all other predictions are assigned the value `0`). By default, only the
        highest probability prediction is considered. This parameter is ignored
        if `preds` does not contain floating point values.
    average : {'micro', 'macro', 'weighted', 'none'}, optional, default='macro'
        Specifies the type of averaging to apply to the accuracy scores. Should be one
        of the following:
        - `'micro'`: Compute the accuracy score globally by considering all predictions
            and all targets.
        - `'macro'`: Compute the accuracy score for each label individually and then
            take the unweighted mean of the accuracy scores.
        - `'weighted'`: Compute the accuracy score for each label individually and then
            take the mean of the accuracy scores weighted by the support (the number of
            true positives + the number of false negatives) for each label.
        - `'none'` or `None`: Compute the accuracy score for each label individually
            and return the scores as an array.
    ignore_index : int, optional, default=None
        Specifies a value in the target array(s) that is ignored when computing
        the accuracy score.

    Examples
    --------
    >>> from cyclops.evaluate.metrics.experimental import MultilabelAccuracy
    >>> import numpy.array_api as anp
    >>> target = anp.asarray([[0, 1, 1], [1, 0, 0]])
    >>> preds = anp.asarray([[0, 1, 0], [1, 0, 1]])
    >>> metric = MultilabelAccuracy(num_labels=3)
    >>> metric(target, preds)
    Array(0.6666667, dtype=float32)
    >>> metric.reset()
    >>> target = [[[0, 1, 1], [1, 0, 0]], [[1, 0, 0], [0, 1, 1]]]
    >>> preds = [[[0.05, 0.95, 0], [0.1, 0.8, 0.1]], [[0.1, 0.8, 0.1], [0.05, 0.95, 0]]]
    >>> for t, p in zip(target, preds):
    ...     metric.update(anp.asarray(t), anp.asarray(p))
    >>> metric.compute()
    Array(0.5, dtype=float32)

    """

    name: str = "Accuracy Score"

    def _compute_metric(self) -> Array:
        """Compute the accuracy score."""
        tn, fp, fn, tp = self._final_state()
        return _accuracy_compute(
            tp=tp,
            fp=fp,
            tn=tn,
            fn=fn,
            is_multilabel=True,
            average=self.average,
        )
