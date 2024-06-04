#!/usr/bin/python

# pylmm is a python-based linear mixed-model solver with applications to GWAS
# Copyright (C) 2015  Nicholas A. Furlotte (nick.furlotte@gmail.com)

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from pylmm3 import input
from pylmm3.lmm import calculateKinship
from scipy import linalg
import numpy as np
import os
import sys
import pdb

from optparse import OptionParser, OptionGroup


def main(): 
    usage = """usage: %prog [options] --[tfile | bfile] plinkFileBase outfile"""

    parser = OptionParser(usage=usage)

    basicGroup = OptionGroup(parser, "Basic Options")
    # advancedGroup = OptionGroup(parser, "Advanced Options")

    # basicGroup.add_option("--pfile", dest="pfile",
    #                  help="The base for a PLINK ped file")
    basicGroup.add_option("--tfile", dest="tfile",
                        help="The base for a PLINK tped file")
    basicGroup.add_option("--bfile", dest="bfile",
                        help="The base for a PLINK binary ped file")
    basicGroup.add_option(
        "--emmaSNP",
        dest="emmaFile",
        default=None,
        help="For backwards compatibility with emma, we allow for \"EMMA\" file formats.  This is just a text file with individuals on the rows and snps on the columns.")
    basicGroup.add_option(
        "--emmaNumSNPs",
        dest="numSNPs",
        type="int",
        default=0,
        help="When providing the emmaSNP file you need to specify how many snps are in the file")

    basicGroup.add_option(
        "-e",
        "--efile",
        dest="saveEig",
        help="Save eigendecomposition to this file.")
    basicGroup.add_option(
        "-n",
        default=1000,
        dest="computeSize",
        type="int",
        help="The maximum number of SNPs to read into memory at once (default 1000).  This is important when there is a large number of SNPs, because memory could be an issue.")

    basicGroup.add_option("-v", "--verbose",
                        action="store_true", dest="verbose", default=False,
                        help="Print extra info")

    parser.add_option_group(basicGroup)
    # parser.add_option_group(advancedGroup)

    (options, args) = parser.parse_args()
    if len(args) != 1:
        parser.print_help()
        sys.exit()

    outFile = args[0]


    if not options.tfile and not options.bfile and not options.emmaFile:
        parser.error(
            "You must provide at least one PLINK input file base (--tfile or --bfile) or an emma formatted file (--emmaSNP).")

    if options.verbose:
        sys.stderr.write("Reading PLINK input...\n")
    if options.bfile:
        IN = input.plink(options.bfile, type='b')
    elif options.tfile:
        IN = input.plink(options.tfile, type='t')
    # elif options.pfile: IN = input.plink(options.pfile,type='p')
    elif options.emmaFile:
        if not options.numSNPs:
            parser.error(
                "You must provide the number of SNPs when specifying an emma formatted file.")
        IN = input.plink(options.emmaFile, type='emma')
    else:
        parser.error(
            "You must provide at least one PLINK input file base (--tfile or --bfile) or an emma formatted file (--emmaSNP).")

    n = len(IN.indivs)
    m = options.computeSize
    W = np.ones((n, m)) * np.nan

    IN.getSNPIterator()
    # Annoying hack to get around the fact that it is expensive to determine
    # the number of SNPs in an emma file
    if options.emmaFile:
        IN.numSNPs = options.numSNPs
    i = 0
    K = None
    while i < IN.numSNPs:
        j = 0
        while j < options.computeSize and i < IN.numSNPs:
            snp, id = next(IN)  # Changed from IN.next() to next(IN)
            if snp.var() == 0:
                i += 1
                continue
            W[:, j] = snp

            i += 1
            j += 1
        if j < options.computeSize:
            W = W[:, range(0, j)]

        if options.verbose:
            sys.stderr.write("Processing first %d SNPs\n" % i)
        if K is None:
            try:
                K = linalg.fblas.dgemm(
                    alpha=1.,
                    a=W.T,
                    b=W.T,
                    trans_a=True,
                    trans_b=False)  # calculateKinship(W) * j
            except AttributeError:
                K = np.dot(W, W.T)
        else:
            try:
                K_j = linalg.fblas.dgemm(
                    alpha=1.,
                    a=W.T,
                    b=W.T,
                    trans_a=True,
                    trans_b=False)  # calculateKinship(W) * j
            except AttributeError:
                K_j = np.dot(W, W.T)
            K = K + K_j

    K = K / float(IN.numSNPs)
    if options.verbose:
        sys.stderr.write("Saving Kinship file to %s\n" % outFile)
    np.savetxt(outFile, K)

    if options.saveEig:
        if options.verbose:
            sys.stderr.write("Obtaining Eigendecomposition\n")
        Kva, Kve = linalg.eigh(K)
        if options.verbose:
            sys.stderr.write(
                "Saving eigendecomposition to %s.[kva | kve]\n" %
                outFile)
        np.savetxt(outFile + ".kva", Kva)
        np.savetxt(outFile + ".kve", Kve)


if __name__ == "__main__":
    main()
