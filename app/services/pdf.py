
from typing import Annotated
from fastapi import APIRouter, File, UploadFile, Request, Form, HTTPException, Header
from app.utils.parse_pdf import parse_pdf
from app.setup.vdb import store_chunks_in_chroma, load_vectorstore, get_uploaded_pdfs
from app.utils.chain import ask_in_pdf, summarize_pdf
from app.utils.hash import get_pdf_hash
from uuid import uuid4
from app.models.pdf import AskQuestion

def upload_pdf_service(filename : str, pdf_bytes: bytes) -> str:
    pdf_hash = get_pdf_hash(pdf_bytes)

    pdf_chunks = parse_pdf(pdf_bytes, chunk_it=True)

    stored = store_chunks_in_chroma(pdf_chunks, pdf_id=pdf_hash)

    if not stored:
        return {
            "message" : "PDF already uploaded.",
            "filename" : filename,
            "pdf_id" : pdf_hash,
        }

    return {
        "message" : "PDF uploaded successfully.",
        "filename" : filename, 
        "pdf_id" : pdf_hash,
    }

def ask_question_service(question : str, pdf_id : str) -> str:
    vectorstore = load_vectorstore(pdf_id)

    if not vectorstore:
        raise HTTPException(status_code=404, detail="PDF not found. Please upload a PDF file.")

    answer = ask_in_pdf(vectorstore, question)
    
    return answer

def summarize_pdf_service(pdf_id : str) -> str:
    vectorstore = load_vectorstore(pdf_id)
    summary = summarize_pdf(vectorstore)

    return summary