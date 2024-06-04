"""Utility functions for metrics."""

from typing import (
    Any,
    Callable,
    List,
    Literal,
    Mapping,
    Optional,
    Sequence,
    Tuple,
    Union,
)

import numpy as np
import numpy.typing as npt
from sklearn.utils.multiclass import type_of_target


# boolean, unsigned integer, signed integer, float, complex.
_NUMERIC_KINDS = set("buifc")


def is_numeric(*arrays: npt.ArrayLike) -> bool:
    """Check if given arrays have numeric datatype.

    Determine whether the argument(s) have a numeric datatype, when converted to a
    NumPy array. Booleans, unsigned integers, signed integers, floats and complex
    numbers are the kinds of numeric datatype.

    Parameters
    ----------
    arrays: array-likes
        The arrays to check.

    Returns
    -------
    is_numeric: ``bool``
        True if all of the arrays have a numeric datatype, False if not.

    """
    return all(np.asanyarray(array).dtype.kind in _NUMERIC_KINDS for array in arrays)


def _adjust_dim(inp: npt.NDArray[Any]) -> npt.NDArray[Any]:
    """Adjust the dimension of the input."""
    if inp.ndim == 0:
        inp = np.expand_dims(inp, axis=0)

    return inp


def _check_input_dims(*arrays: npt.NDArray[Any]) -> None:
    """Check the dimensions of the input arrays.

    Singleton arrays and arrays with more than two dimensions are not allowed.

    Parameters
    ----------
    arrays: numpy.ndarray
        The arrays to check.

    Raises
    ------
    ValueError
        If any of the input arrays have more than two dimensions or if the

    """
    for array in arrays:
        if array.ndim == 0 or array.ndim > 2:
            raise ValueError(
                f"Input contains {array.ndim} dimensions, but only 1 or 2 dimensional "
                "arrays are supported.",
            )


def common_input_checks_and_format(
    target: npt.ArrayLike,
    preds: npt.ArrayLike,
) -> Tuple[npt.NDArray[Any], npt.NDArray[Any], str, str]:
    """Check the input and convert it to the correct format.

    This function also checks if the input is valid.

    Parameters
    ----------
    target: ArrayLike
        The target.
    preds: ArrayLike
        The predictions.

    Returns
    -------
    target: np.ndarray
        The target as a numpy array.
    preds: np.ndarray
        The predictions as a numpy array.
    type_target: str
        The type of the target. One of:

    * 'continuous': ``target`` is an array-like of floats that are not all
        integers, and is 1d or a column vector.
    * 'continuous-multioutput': ``target`` is a 2d array of floats that are
        not all integers, and both dimensions are of size > 1.
    * 'binary': ``target`` contains <= 2 discrete values and is 1d or a column
        vector.
    * 'multiclass': ``target`` contains more than two discrete values, is not a
        sequence of sequences, and is 1d or a column vector.
    * 'multiclass-multioutput': ``target`` is a 2d array that contains more
        than two discrete values, is not a sequence of sequences, and both
        dimensions are of size > 1.
    * 'multilabel-indicator': ``target`` is a label indicator matrix, an array
        of two dimensions with at least two columns, and at most 2 unique
        values.
    * 'unknown': ``target`` is array-like but none of the above, such as a 3d
        array, sequence of sequences, or an array of non-sequence objects.

    type_preds: str
        The type of the predictions.

    Raises
    ------
    ValueError
        If the input has more than two dimensions.

    """
    target, preds = np.asanyarray(target), np.asanyarray(preds)

    if not is_numeric(target, preds):
        raise ValueError("The input `target` and `preds` must be numeric.")

    target = _adjust_dim(target)
    preds = _adjust_dim(preds)

    _check_input_dims(target, preds)  # only 1D or 2D arrays are allowed

    type_target = type_of_target(target)
    type_preds = type_of_target(preds)

    return target, preds, type_target, type_preds


def sigmoid(arr: npt.ArrayLike) -> npt.NDArray[np.float_]:
    """Sigmoid function."""
    arr = np.asanyarray(arr)
    return 1 / (1 + np.exp(-arr))  # type: ignore


def check_topk(top_k: int, type_preds: str, type_target: str, n_classes: int) -> None:
    """Check if top_k is valid.

    Parameters
    ----------
    top_k: int
        The number of classes to select.
    type_preds: str
        The type of the predictions.
    type_target: str
        The type of the target.
    n_classes: int
        The number of classes.

    Raises
    ------
    ValueError
        If top_k is not valid.

    """
    if type_target == "binary":
        raise ValueError("You can not use `top_k` parameter with binary data.")
    if type_preds not in ["continuous", "continuous-multioutput"]:
        raise ValueError("You can only use `top_k` with continuous predictions.")
    if not isinstance(top_k, int) or top_k <= 0:
        raise ValueError("The `top_k` has to be an integer larger than 0.")
    if top_k >= n_classes:
        raise ValueError(
            "The `top_k` has to be strictly smaller than the number of classes.",
        )


def select_topk(
    prob_scores: npt.ArrayLike,
    top_k: Optional[int] = 1,
) -> npt.NDArray[np.int_]:
    """Convert a probability scores to binary by selecting top-k highest entries.

    Parameters
    ----------
    prob_scores : ArrayLike
        The probability scores. Must be a 2D array.
    top_k : int, default=1
        The number of top predictions to select.

    Returns
    -------
    np.ndarray
        A binary ndarray of the same shape as the input array.

    """
    if top_k == 1:
        topk_indices = np.argmax(prob_scores, axis=-1, keepdims=True)
    else:
        topk_indices = np.argsort(prob_scores, axis=-1)[:, ::-1][
            :,
            :top_k,
        ]  # sort in descending order, then slice the top k

    topk_array = np.zeros_like(prob_scores)
    np.put_along_axis(topk_array, topk_indices, 1.0, axis=-1)

    return topk_array.astype(np.int_)


def _check_thresholds(
    thresholds: Optional[Union[int, List[float], npt.NDArray[np.float_]]],
) -> None:
    """Check if thresholds are valid.

    Parameters
    ----------
    thresholds : Union[int, List[float], np.ndarray]
        Thresholds used for computing the precision and recall scores.
        Can be either an integer, a list of floats, a numpy array or None.

    Returns
    -------
    None

    Raises
    ------
    ValueError
        If ``thresholds`` is not None, an integer, a list of floats or a numpy
        array.
    ValueError
        If ``thresholds`` is an integer and is less than 2.
    ValueError
        If ``thresholds`` is a list or numpy array and does not contain floats
        in the range [0, 1].
    ValueError
        If ``thresholds`` is a numpy array and is not a 1D array.
    ValueError
        If ``thresholds`` is a list or numpy array and the values are not
        monotonically increasing.

    """
    if thresholds is not None and not isinstance(thresholds, (int, list, np.ndarray)):
        raise ValueError(
            "Expected argument `thresholds` to either be an integer, list of floats or"
            f" np.ndarray of floats, but got {thresholds}",
        )
    if isinstance(thresholds, int) and thresholds < 2:
        raise ValueError(
            "If argument `thresholds` is an integer, expected it to be "
            f"larger than 1, but got {thresholds}",
        )
    if isinstance(thresholds, (list, np.ndarray)) and not all(
        isinstance(t, float) and 0 <= t <= 1 for t in thresholds
    ):
        raise ValueError(
            "If argument `thresholds` is a list, expected all elements to be "
            f"floats in the [0,1] range, but got {thresholds}",
        )
    if isinstance(thresholds, np.ndarray) and not thresholds.ndim == 1:
        raise ValueError(
            "If argument `thresholds` is a numpy array, expected the array to be 1d",
        )
    if isinstance(thresholds, (list, np.ndarray)) and not all(np.diff(thresholds) > 0):
        raise ValueError(
            "Expected argument `thresholds` to be monotonically increasing,"
            f" but got {thresholds}",
        )


def _check_average_arg(average: Literal["micro", "macro", "weighted", None]) -> None:
    """Validate the ``average`` argument."""
    if average not in ["micro", "macro", "weighted", None]:
        raise ValueError(
            f"Argument average has to be one of 'micro', 'macro', 'weighted', "
            f"or None, got {average}.",
        )


def _apply_function_recursively(
    data: Any,
    func: Callable[..., Any],
    *args: Any,
    **kwargs: Any,
) -> Any:
    """Apply a function recursively to a given data structure.

    Parameters
    ----------
    data : Any
        The data structure to apply the function to.
    func : Callable
        The function to apply to the data structure.
    *args : Any
        Additional positional arguments to pass to the function.
    **kwargs : Any
        Additional keyword arguments to pass to the function.

    Returns
    -------
    The data structure with the function applied to it.

    """
    data_type = type(data)
    is_namedtuple_ = (
        isinstance(data, tuple)
        and hasattr(data, "_asdict")
        and hasattr(data, "_fields")
    )
    is_sequence = isinstance(data, Sequence) and not isinstance(data, str)
    if is_namedtuple_ or is_sequence:
        out = [_apply_function_recursively(el, func, *args, **kwargs) for el in data]
        return data_type(*out) if is_namedtuple_ else data_type(out)
    if isinstance(data, Mapping):
        return data_type(
            {
                k: _apply_function_recursively(v, func, *args, **kwargs)
                for k, v in data.items()
            },
        )
    return func(data)


def _get_value_if_singleton_array(
    data: npt.ArrayLike,
) -> Union[npt.ArrayLike, Any]:
    """Return element if input is 0d or 1d singleton array-like object."""
    data_arr = np.asanyarray(data)
    return data_arr.item() if (data_arr.ndim == 0 or data_arr.size == 1) else data
