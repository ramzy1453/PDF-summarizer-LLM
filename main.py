from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from app.routers.pdf import router as pdf_router

app = FastAPI()
app.mount("/media", StaticFiles(directory=Path('media')), name="media")


@app.get("/")
def api():
    return {"message": "PDF Summarizer API v1.0"}

app.include_router(pdf_router, prefix="/api/v1/pdf", tags=["pdf"])