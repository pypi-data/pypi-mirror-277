import copy

def clone(estimator, *, safe=True):
    """Construct a new unfitted estimator with the same parameters.

    Clone does a deep copy of the model in an estimator
    without actually copying attached data. It returns a new estimator
    with the same parameters that has not been fitted on any data.

    .. versionchanged:: 1.3
        Delegates to `estimator.__sklearn_clone__` if the method exists.

    Parameters
    ----------
    estimator : {list, tuple, set} of estimator instance or a single \
            estimator instance
        The estimator or group of estimators to be cloned.
    safe : bool, default=True
        If safe is False, clone will fall back to a deep copy on objects
        that are not estimators. Ignored if `estimator.__sklearn_clone__`
        exists.

    Returns
    -------
    estimator : object
        The deep copy of the input, an estimator if input is an estimator.

    Notes
    -----
    If the estimator's `random_state` parameter is an integer (or if the
    estimator doesn't have a `random_state` parameter), an *exact clone* is
    returned: the clone and the original estimator will give the exact same
    results. Otherwise, *statistical clone* is returned: the clone might
    return different results from the original estimator. More details can be
    found in :ref:`randomness`.

    Examples
    --------
    >>> from sklearn.base import clone
    >>> from sklearn.linear_model import LogisticRegression
    >>> X = [[-1, 0], [0, 1], [0, -1], [1, 0]]
    >>> y = [0, 0, 1, 1]
    >>> classifier = LogisticRegression().fit(X, y)
    >>> cloned_classifier = clone(classifier)
    >>> hasattr(classifier, "classes_")
    True
    >>> hasattr(cloned_classifier, "classes_")
    False
    >>> classifier is cloned_classifier
    False
    """
    if safe:
        return copy.deepcopy(estimator)
    else:
        return copy.copy(estimator)
