""""

Usage:
    pdf_splitter.py <source_file>

Arguments:
    source_file                     Path to source file

"""
import os

from PyPDF2 import PdfFileWriter, PdfFileReader
from docopt import docopt

# read passed in arguments
args = docopt(__doc__)
# set source_path with passed in path
source_file = args['<source_file>']
dest_folder = source_file[:source_file.rfind("/")] + "/"

PDF_filename = source_file[source_file.rfind("/")+1:source_file.rfind(".")]
source_PDF = PdfFileReader(open(source_file, "rb"))

for i in range(source_PDF.numPages):
    output = PdfFileWriter()
    output.addPage(source_PDF.getPage(i))
    os.chdir(dest_folder)
    # for debugging directory, uncomment the following line
    # print(os.getcwd())
    with open(PDF_filename + " - Page %s.pdf" % (i+1), "wb") as outputStream:
        output.write(outputStream)
