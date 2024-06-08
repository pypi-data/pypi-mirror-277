"""
"""

import sys

from gbtgridder import gbtgridder, gbtgridder_args


def grid(args):
    """
    """
    gbtgridder.gbtgridder(args)


def parse_args(filename, base, average=None, 
               overwrite=False, diameter=20,
               size=None, x=None, y=None, 
               pixelwidth=None,
               verbose=4):
    """
    """

    sys.argv = [sys.argv[0]]
    sys.argv.append(filename)
    sys.argv.append("-o")
    sys.argv.append(base)
    sys.argv.append("--diameter")
    # Even though this is a float, it 
    # needs to be wrapped as a string.
    sys.argv.append(f"{diameter}")
    if average:
        sys.argv.append("-a")
        sys.argv.append(f"{average}")
    if overwrite:
        sys.argv.append("--clobber")
    if size is not None:
        sys.argv.append("--size")
        sys.argv.append(f"{size[0]}")
        sys.argv.append(f"{size[1]}")
    if pixelwidth is not None:
        sys.argv.append("--pixelwidth")
        sys.argv.append(f"{pixelwidth}")
    #sys.argv.append("--autoConfirm")
    sys.argv.append("-v")
    sys.argv.append(f"{verbose}")
    
    return sys.argv


def main(filename, base, average=None, 
         overwrite=False, diameter=20, 
         size=None, pixelwidth=None,
         verbose=4):
    """
    """

    args = parse_args(filename, base, average=average, 
                      overwrite=overwrite, diameter=diameter,
                      size=size, pixelwidth=pixelwidth,
                      verbose=verbose)
    args = gbtgridder_args.parser_args(args, "2.0")
    gbtgridder_args.check_args(args)
    grid(args)

