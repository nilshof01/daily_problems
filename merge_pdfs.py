import PyPDF4
from tkinter.filedialog import askdirectory
from os.path import join
import glob


def merge_pdfs():
    print("Choose the directory where you store the pdfs. Make sure that the directory contains only the files you want to merge.")
    directory = askdirectory()
    filenames = glob.glob(join(directory, "*.pdf"))

    # Create a new PDF file
    pdf_writer = PyPDF4.PdfFileWriter()

    # Add the pages of all PDF files to the new PDF file
    for filename in filenames:
        pdf = open(filename, 'rb')
        pdf_reader = PyPDF4.PdfFileReader(pdf)
        for page_num in range(pdf_reader.getNumPages()):
            page = pdf_reader.getPage(page_num)
            pdf_writer.addPage(page)


    # Save the new PDF file
    merged_pdf = open('merged_file.pdf', 'wb')
    pdf_writer.write(merged_pdf)
    merged_pdf.close()


if __name__ == '__main__':
    merge_pdfs()
