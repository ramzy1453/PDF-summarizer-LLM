
from typing import Annotated
from fastapi import APIRouter, File, UploadFile
from app.utils.parse_pdf import parse_pdf

router = APIRouter()


@router.post("/summarize")
async def create_upload_file(file: UploadFile):
    try:
        if file.content_type != "application/pdf":
            return {"error": "Invalid file type uploaded. Please upload a PDF file."}
        
        pdf_bytes = await file.read()
        pdf_content = parse_pdf(pdf_bytes)
        
        return {"filename" : file.filename, "content" : pdf_content}
    except Exception as e:
        return {"error": str(e)}