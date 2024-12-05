
from typing import Annotated
from fastapi import APIRouter, File, UploadFile
from app.utils.parse_pdf import parse_pdf
from app.setup.vdb import store_chunks_in_chroma
from app.utils.chain import create_chain

router = APIRouter()


@router.post("/upload_pdf")
async def upload_pdf_file(file: UploadFile):
    try:
        if file.content_type != "application/pdf":
            return {"error": "Invalid file type uploaded. Please upload a PDF file."}
        
        pdf_bytes = await file.read()
        pdf_chunks = parse_pdf(pdf_bytes)

        vectorstore = store_chunks_in_chroma(pdf_chunks, 'id_1')

        qa_chain = create_chain(vectorstore)

        response = qa_chain.invoke({ 
            "task_type": "answer a question",
            "input": ""
        })
        
        return {"filename" : file.filename, "chunks" : len(pdf_chunks) , "answer" : response,  "content" : pdf_chunks}
    except Exception as e:
        return {"error": str(e)}