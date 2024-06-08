import typing as t


def is_nested_iterable(value: t.Any) -> bool:
    """
    Checks if the given value is an iterable of iterables.

    Parameters
    ----------
    value : Any
        The value to be checked.

    Returns
    -------
    bool
        True if the value is an iterable of iterables, False otherwise.
    """
    if isinstance(value, t.Iterable):
        for item in value:
            if not isinstance(item, t.Iterable):
                return False
        return True
    return False
