from pydantic import BaseModel

class AskQuestion(BaseModel):
    question: str