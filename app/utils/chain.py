from langchain.schema.output_parser import StrOutputParser
from langchain.chains.llm import LLMChain
from langchain.schema.runnable import RunnableMap
from langchain.vectorstores import Chroma
from app.setup.llm import llm
from app.prompts.prompt import ask_prompt, summarize_prompt

output_parser = StrOutputParser()
summarize_chain = summarize_prompt | llm | output_parser

def summarize_pdf(vectorstore : Chroma) -> str:

    response = summarize_chain.invoke({
        "context": ' '.join(vectorstore.get()["documents"]),
    })

    return response


def create_ask_chain(vectorstore : Chroma) -> RunnableMap:
    retriever = vectorstore.as_retriever()

    chain = RunnableMap({
        "context": lambda x: retriever.invoke(x["input"]),
        "input": lambda x: x["input"],
    }) | ask_prompt | llm | output_parser

    return chain