
__version__ = "1.5"

all = ["version", "main"]


def version():
    """Version of the code

    Returns
    -------
    version : str
        Package version.
    """
    return __version__


from . import gbtgridder


def main():
    gbtgridder.main()
