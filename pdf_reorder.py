"""reorder pages in a pdf file where first the odd pages 1,3,5,7...99 were scanned
and then the the even pagesin reverse order 100,98,96...2
"""

from PyPDF2 import PdfReader, PdfWriter
import pathlib as pl

# use tka as a simple graphical user interface for opening input and output file

from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

# Open file dialog to select input file
input_file_path = askopenfilename(
    title="Select input pdf file to be reordered",
    filetypes=[("PDF Files", "*.pdf")]
)

path_to_file = pl.Path(input_file_path)

# read the input pdf file and write the reordered pdf file
with open(input_file_path, 'rb') as input_file:
    read_pdf = PdfReader(input_file)  # read_pdf is a PdfFileReader object
    number_of_pages = len(read_pdf.pages)
    print(number_of_pages)
    if number_of_pages % 2 != 0:
        print("Number of pages is not even. Exiting.")
        exit(1)
    # open the writer PDF File in memory
    write_pdf = PdfWriter()
    # write the reordered pages
    for page in range(number_of_pages//2):
        write_pdf.add_page(read_pdf.pages[page])
        write_pdf.add_page(read_pdf.pages[number_of_pages - page - 1])

    initial_file_name = path_to_file.stem+"_REordered.pdf"
    output_file_path = asksaveasfilename(
        defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")],
        initialfile=initial_file_name)

    with open(output_file_path, "wb") as output_file:
        write_pdf.write(output_file)
