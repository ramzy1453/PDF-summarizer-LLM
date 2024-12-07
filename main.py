from fastapi import FastAPI
import uvicorn

from app.routers.pdf import router as pdf_router

app = FastAPI()

@app.get("/")
def api():
    return {"message": "Hello World"}

app.include_router(pdf_router, prefix="/api/v1/pdf", tags=["pdf"])