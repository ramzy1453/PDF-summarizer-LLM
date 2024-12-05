from langchain.prompts import ChatPromptTemplate

template = """You are an expert assistant trained to analyze PDF documents. The user will provide a PDF, and your task is to do one of the following based on the user's request:

1. Summarize the PDF content.
2. Answer a specific question about the PDF content.

Here is the content extracted from the PDF:
{context}

### User's Request
The user wants you to: {task_type}

- If the task is "Summarize," provide a concise summary (max 200 words).
- If the task is "Answer a Question," provide a precise response to the question.

### User's Question (if applicable)
{input}

### Your Response:
(Your response goes here)
"""


prompt = ChatPromptTemplate.from_template(template)