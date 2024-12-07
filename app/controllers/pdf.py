from typing import Annotated
from fastapi import APIRouter, File, UploadFile, Request, Form, HTTPException, Header
from app.utils.parse_pdf import parse_pdf
from app.setup.vdb import store_chunks_in_chroma, load_vectorstore, get_uploaded_pdfs
from app.utils.chain import ask_in_pdf, summarize_pdf
from app.utils.hash import get_pdf_hash
from uuid import uuid4
from app.models.pdf import AskQuestion
from app.services.pdf import *

async def upload_pdf_controller(pdf: UploadFile):
    try:
        if pdf.content_type != "application/pdf":
            raise HTTPException(status_code=404, detail="Invalid file type uploaded. Please upload a PDF file.")
        
        pdf_bytes = await pdf.read()
        response = upload_pdf_service(pdf.filename, pdf_bytes)
        return response
    
    except Exception as e:
        return {"error": str(e)}

def ask_question_controller(body : AskQuestion, pdf_id : str):
    try:

        question = body.question
        answer = ask_question_service(question, pdf_id)
        
        return {
            "answer" : answer
        }

    except Exception as e:
        return {"error": str(e)}

def summarize_controller(pdf_id : str):
    
    try:
        summary = summarize_pdf_service(pdf_id)
        return {"summary" : summary}

    except Exception as e:
        return {"error": str(e)}

def uploaded_pdfs_controller():
    try:
        return {"pdfs" : get_uploaded_pdfs()}
    except Exception as e:
        return {"error": str(e)}