"""
Separates the contents of a 20m SDFITS file
into spectral windows and polarizations.
"""

import os
import sys
import argparse
import warnings

from astropy.io import fits
from dysh.fits.gb20mfitsload import GB20MFITSLoad
from astropy.utils.exceptions import AstropyWarning, AstropyDeprecationWarning

from grid20m.cli_args import (cli_arguments, 
                              parse_arg_output)


def parse_sdf(sdf):
    """
    Checks the contents of the SDFITSFile
    and sets how many output files will be produced.
    """

    nbin = len(sdf.bintable)
    pols = []
    npol = []
    spws = []
    nspw = []
    for i in range(nbin):
        pols.append(sdf.udata("PLNUM"))
        npol.append(len(pols[i]))
        spws.append(sdf.udata("IFNUM"))
        nspw.append(len(spws[i]))

    out = {"nbin": nbin,
           "npol": npol,
           "nspw": nspw,
           "pols": pols,
           "spws": spws,
           }

    return out


def select_sdf_rows(sdf, query, bintable=0):
    """
    """

    return sdf._index.query(query).index
    

def build_query(ifnum, plnum):
    """
    """

    return f"PLNUM in [{plnum}] and IFNUM in [{ifnum}]"


def default_output_name(base, hdu, spw, pl):
    """
    """

    return f"{base}_hdu_{hdu}_spw_{spw}_plnum_{pl}.fits"


def split_sdf(sdf, numbers, base=None, overwrite=False):
    """
    """

    output = lambda hdu, spw, pl: default_output_name(base, hdu, spw, pl)
    outputs = []

    for b in range(numbers["nbin"]):
        for s in numbers["spws"][b]:
            for p in numbers["pols"][b]:
                this_output = output(b+1, s, p)
                query = build_query(s, p)
                rows = select_sdf_rows(sdf, query, bintable=b)
                print(f"Saving spectral window {s} polarization {p} to {this_output}")
                sdf.write(this_output, rows=rows, bintable=b, 
                          overwrite=overwrite)
                outputs.append(this_output)

    return outputs


def patch_obsmode(sdfitsfile):
    """
    Updates the OBSMODE column with the header value.
    """

    hdu = fits.open(sdfitsfile, mode="update")
    head = hdu[0].header
    table = hdu[1].data
    table["OBSMODE"] = head["OBSMODE"]
    hdu.flush()
    hdu.close()


def main(sdfitsfile, basename, overwrite=False):
    """
    """
    patch_obsmode(sdfitsfile)
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', AstropyWarning)
        warnings.simplefilter('ignore', AstropyDeprecationWarning)
        print(f"Loading: {sdfitsfile}")
        sdf = GB20MFITSLoad(sdfitsfile, index=False)
        numbers = parse_sdf(sdf)
        split_sdfs = split_sdf(sdf, numbers, basename, overwrite)

    return split_sdfs


def cli_main():
    """
    Starting point if calling from the command line.
    """
    args = cli_arguments()
    basename = parse_arg_output(args)
    main(args.SDFITSFile, basename, args.overwrite)


if __name__ == "__main__":
    cli_main()
