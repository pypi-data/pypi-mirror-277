"""
"""

import os

from grid20m import split
from grid20m import grid
from grid20m import cli_args


def cli_main():
    """
    """

    args = cli_args.cli_arguments()
    main(args)


def main(args):
    """
    """

    basename = cli_args.parse_arg_output(args)
    split_sdfs = split.main(args.SDFITSFile, basename, overwrite=args.overwrite)
    for sdf in split_sdfs:
        base = os.path.splitext(sdf)[0]
        grid.main(sdf, base, average=args.average, 
                  overwrite=args.overwrite, diameter=20,
                  size=args.size, pixelwidth=args.pixelwidth,
                  verbose=args.verbose)



if __name__ == "__main__":
    cli_main()
