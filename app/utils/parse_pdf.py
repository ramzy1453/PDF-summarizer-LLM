from fastapi import UploadFile
from PyPDF2 import PdfReader
import io


def parse_pdf(pdf_bytes : bytes) -> str:
    
    pdf_reader = PdfReader(io.BytesIO(pdf_bytes))

    pdf_text = ""
    for page in pdf_reader.pages:
        pdf_text += page.extract_text()

    return pdf_text