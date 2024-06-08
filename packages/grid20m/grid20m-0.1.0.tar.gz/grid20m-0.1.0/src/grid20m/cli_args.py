"""
"""

import os
import argparse


def cli_arguments():
    """
    """

    parser = argparse.ArgumentParser(
           epilog="Split 20m"
    )

    parser.add_argument("SDFITSFile",
                        type=str,
                        help="The SDFITSFile to split."
                       )

    parser.add_argument("-o", "--output", type=str,
                        help="Output filename.")

    parser.add_argument("-a", "--average", type=int,
                        help="Average this many channels during gridding.")

#    parser.add_argument("-s", "--scans", type=str,
#                        help="Scans to split.")
#
#    parser.add_argument("-w", "--windows", type=str,
#                        help="Spectral windows to split.")
#
#    parser.add_argument("-p", "--polarizations", type=str,
#                        help="Polarizations to split.")

    parser.add_argument("--size", type=int,
                        metavar=("X", "Y"),
                        nargs=2,
                        help="Output cube size in pixels."
                             "By default it will use a size "
                             "that covers the mapped area."
                        )

    parser.add_argument("--pixelwidth", type=float,
                        help="Image pixel width on sky (arcsec)."
                             "By default it will use a pixel size "
                             "that samples the beam with three pixels."
                       )

    parser.add_argument("--overwrite", default=False,
                        action="store_true",
                        help="Overwrites existing files if set.")

    parser.add_argument("-v", "--verbose", type=int,
                        default=4, 
                        help="Verbosity level -- 0-1:none, "
                             "2:errors only, 3:+warnings, "
                             "4(default):+user info, 5:+debug"
                       )

    args = parser.parse_args()

    return args


def parse_arg_output(args):
    """
    """

    if args.output is None:
        base = os.path.splitext(args.SDFITSFile)[0]
    else:
        base = args.output

    return base
