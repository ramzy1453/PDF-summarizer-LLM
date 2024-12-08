from pydantic import BaseModel

class AskQuestion(BaseModel):
    question: str
    pdf_id: str

class Summarize(BaseModel):
    pdf_id: str