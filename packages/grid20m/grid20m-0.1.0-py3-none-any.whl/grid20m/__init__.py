"""Top-level package for grid20m."""
__version__ = "0.1.0"

all = ["version"]

def version():
    """Version of the grid20m code
    :rtype: str
    """
    return __version__

"""Classes and functions"""
__all__ = [ "main", "split", "grid", "cli_args" ]
