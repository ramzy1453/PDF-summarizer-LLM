from PyPDF2 import PdfReader
import io
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from typing import List

def parse_pdf(pdf_bytes : bytes, chunk_it : bool = False, chunk_size : int = 200) -> str | List[str]:
    
    pdf_reader = PdfReader(io.BytesIO(pdf_bytes))

    pdf_text = ""
    for page in pdf_reader.pages:
        pdf_text += page.extract_text()

    if not chunk_it:
        return pdf_text

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=40,
    )

    chunks = text_splitter.split_text(pdf_text)

    return chunks