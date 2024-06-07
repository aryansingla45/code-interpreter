import pandas as pd
import pdfplumber
from docx import Document

# Function to read the content of a pdf file
def read_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text


# Function to read the content of an xlsx file

def read_xlsx(file_path):
    df = pd.read_excel(file_path)
    return df.to_string()

# Function to read the content of a csv file
def read_csv(file_path):
    df = pd.read_csv(file_path)
    return df.to_string()

# Function to read the content of a docx file
def read_docx(file_path):
    doc = Document(file_path)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text
