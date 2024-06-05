"""
Example Experimentalist
"""
from typing import Callable

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator


def filter(
    conditions: pd.DataFrame,
    model: BaseEstimator,
    filter_function: Callable,
    reset_index: bool = True,
) -> pd.DataFrame:
    """
    Filter conditions based on the expected outcome io the mdeol

    Args:
        conditions: The pool to filter
        model: The model to make the prediction
        filter_function: A function that returns True if a prediciton should be included

    Returns:
        Filtered pool of experimental conditions

    Examples:
        >>> class ModelLinear:
        ...     def predict(self, X):
        ...         return 2 * X + 1
        >>> model = ModelLinear()
        >>> model.predict(4)
        9

        >>> filter_fct = lambda x: 5 < x < 10
        >>> pool = pd.DataFrame({'x': [1, 2, 3, 4, 5, 6]})
        >>> filter(pool, model, filter_fct)
           x
        0  3
        1  4


    """
    new_conditions = conditions.copy()

    def __filter(x):
        y = model.predict(np.array(x))
        if hasattr(y, "shape") and y.shape == np.array([1]):
            y = y[0]
        _bool = filter_function(y)
        return _bool

    new_conditions["__prediction"] = new_conditions.apply(__filter, axis=1)

    _c = new_conditions[new_conditions["__prediction"]]
    _c = _c.drop(columns=["__prediction"])
    if reset_index:
        _c.reset_index(drop=True, inplace=True)

    return _c


prediction_filter = filter
