from langchain.schema.output_parser import StrOutputParser
from langchain_chroma import Chroma
from app.setup.llm import llm
from app.prompts.prompt import ask_prompt, summarize_prompt

output_parser = StrOutputParser()

summarize_chain = summarize_prompt | llm | output_parser
ask_chain = ask_prompt | llm | output_parser

def summarize_pdf(vectorstore : Chroma) -> str:

    response = summarize_chain.invoke({
        "context": ' '.join(vectorstore.get()["documents"]),
    })

    return response


def ask_in_pdf(vectorstore : Chroma, question : str) -> str:

    retriever = vectorstore.as_retriever()

    response = ask_chain.invoke({
        "context": retriever.invoke(question),
        "question": question
    })

    return response