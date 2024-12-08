
from typing import Annotated
from fastapi import APIRouter, UploadFile 
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