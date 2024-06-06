from .logs import warn as warn

def deprecate_positional_args(f):
    """Deprecate positionals arguments for methods.

    Using the keyword-only argument syntax in pep 3102, arguments after the * will issue
    a warning when passed as a positional argument. Modified from scikit-learn.

    Parameters
    ----------
    f : Callable
        Function to check arguments on.
    """
