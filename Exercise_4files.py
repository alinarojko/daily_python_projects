import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

# Create a list of text filepaths
filepaths = glob.glob("files/*.txt")


for filepath in filepaths:

    # Add a page to the PDF document for each text file
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # Get the filename without the extension
    # and convert it to the title case (e.g. Cat)
    filename = Path(filepath).stem

    # Add the name to the PDF. define type of the text
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"{filename.capitalize()}", ln=1)

    with open(filepath, "r") as file:
        content = file.read()
    pdf.set_font(family="Times", size=16)
    pdf.multi_cell(w=0, h=6, txt=content)

# Produce the pdf file
pdf.output("output.pdf")