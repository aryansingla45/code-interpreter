import PyPDF2
import pandas as pd
import openpyxl
from docx import Document

def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        content = ""
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            content += page.extractText()
    return content

def read_xlsx(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    data = []
    for row in sheet.iter_rows(values_only=True):
        data.append(row)
    return data

def read_csv(file_path):
    df = pd.read_csv(file_path)
    return df.to_string()

def read_docx(file_path):
    doc = Document(file_path)
    content = ""
    for para in doc.paragraphs:
        content += para.text + "\n"
    return content


