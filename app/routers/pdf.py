
from typing import Annotated
from fastapi import APIRouter, File, UploadFile, Request, Form, HTTPException, Header
from app.utils.parse_pdf import parse_pdf
from app.setup.vdb import store_chunks_in_chroma, load_vectorstore, get_uploaded_pdfs
from app.utils.chain import ask_in_pdf, summarize_pdf
from app.utils.hash import get_pdf_hash
from uuid import uuid4
from app.models.pdf import *
from app.controllers.pdf import *

router = APIRouter()

@router.post("/upload")
async def upload_pdf(pdf: UploadFile):
    return await upload_pdf_controller(pdf)

@router.post("/ask")
def ask_question(body : AskQuestion):
    return ask_question_controller(body)

@router.post("/summarize")
def summarize(body : Summarize):
    return summarize_controller(body)


@router.get("/")
def uploaded_pdfs():
    return uploaded_pdfs_controller()