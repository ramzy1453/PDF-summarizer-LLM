
from typing import Annotated
from fastapi import APIRouter, File, UploadFile, Request, Form, HTTPException, Header
from app.utils.parse_pdf import parse_pdf
from app.setup.vdb import store_chunks_in_chroma, load_vectorstore, get_uploaded_pdfs
from app.utils.chain import ask_in_pdf, summarize_pdf
from app.utils.hash import get_pdf_hash
from uuid import uuid4
from app.models.pdf import AskQuestion

router = APIRouter()

@router.post("/upload_pdf")
async def upload_pdf_file(file: UploadFile):
    try:
        if file.content_type != "application/pdf":
            raise HTTPException(status_code=404, detail="Invalid file type uploaded. Please upload a PDF file.")
        
        pdf_bytes = await file.read()
        pdf_hash = get_pdf_hash(pdf_bytes)

        pdf_chunks = parse_pdf(pdf_bytes, chunk_it=True)

        store_chunks_in_chroma(pdf_chunks, pdf_id=pdf_hash)

        return {
            "filename" : file.filename, 
            "chunks" : len(pdf_chunks), 
            "pdf_id" : pdf_hash,
            "message" : "PDF uploaded successfully.",
        }

    except Exception as e:
        return {"error": str(e)}


@router.post("/ask")
async def ask_question(body : AskQuestion, pdf_id : Annotated[str, Header(convert_underscores=True)] = None):

    try:

        question = body.question
        vectorstore = load_vectorstore(pdf_id)


        if not vectorstore:
            raise HTTPException(status_code=404, detail="PDF not found. Please upload a PDF file.")

        answer = ask_in_pdf(vectorstore, question)
        
        return {
            "answer" : answer
        }

    except Exception as e:
        return {"error": str(e)}

@router.post("/summarize")
async def summarize(pdf_id : Annotated[str, Header(convert_underscores=True)] = None):
    try:
        
        vectorstore = load_vectorstore(pdf_id)

        summary = summarize_pdf(vectorstore)

        return {"summary" : summary}
        
    except Exception as e:
        return {"error": str(e)}


@router.get("/uploaded_pdfs")
def uploaded_pdfs():
    return {"pdfs" : get_uploaded_pdfs()}