
import warnings
import functools


def deprecated(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        message = f"This function is deprecated {func.__name__}."

        warnings.simplefilter('always', DeprecationWarning)  # turn off filter
        warnings.warn(message, category=DeprecationWarning, stacklevel=2)
        warnings.simplefilter('default', DeprecationWarning)  # reset filter

        return func(*args, **kwargs)
    return wrapper
