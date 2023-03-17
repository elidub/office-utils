#!/usr/bin/env python
# -*- coding: utf-8 -*-
from argparse import ArgumentParser
from glob import glob
from PyPDF2 import PdfFileMerger
import os
from pathlib import Path

def merge(path, output_filename):
    home_path = os.path.expanduser('~')
    merger = PdfFileMerger(strict=False)
    for pdffile in glob(home_path + os.sep + path + os.sep + '*.pdf'):
        if pdffile == output_filename:
            continue
        print(f"Appending: '{pdffile}'")
        bookmark = os.path.basename(pdffile[:-4])
        merger.append(pdffile, bookmark)
    output_path = os.path.join(home_path, path, output_filename)
    
    if Path(output_path).is_file():
        raise FileExistsError(f"File '{output_path}' already exists.")
    else:
        print(f'Saving merged PDF to: {output_path}')
    merger.write(output_path)
    merger.close()

if __name__ == "__main__":
    parser = ArgumentParser()
    # Add more options if you like
    parser.add_argument("-o", "--output",
                        dest="output_filename",
                        default="merged.pdf",
                        help="write merged PDF to FILE",
                        metavar="FILE")
    parser.add_argument("-p", "--path",
                        dest="path",
                        default=".",
                        help="path of source PDF files")
    args = parser.parse_args()
    merge(args.path, args.output_filename)