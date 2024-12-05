from PyPDF2 import PdfReader
import io
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS

def parse_pdf(pdf_bytes : bytes) -> str:
    
    pdf_reader = PdfReader(io.BytesIO(pdf_bytes))

    pdf_text = ""
    for page in pdf_reader.pages:
        pdf_text += page.extract_text()

    pdf_text = pdf_text.replace("\n", "")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=40,
    )

    chunks = text_splitter.split_text(pdf_text)

    return chunks