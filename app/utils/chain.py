from langchain.schema.output_parser import StrOutputParser
from langchain.chains.llm import LLMChain
from langchain.schema.runnable import RunnableMap
from langchain.vectorstores import Chroma
from app.setup.llm import llm
from app.prompts.prompt import prompt

def create_chain(vectorstore : Chroma, task_type : str = 'summarize') -> RunnableMap:
    output_parser = StrOutputParser()
    retriever = vectorstore.as_retriever()

    def context_fn(x):
        print(x, retriever.invoke(x["input"]))
        return retriever.invoke(x["input"])

    chain = RunnableMap({
        "context": context_fn,
        "input": lambda x: x["input"],
        "task_type": lambda x: task_type,
    }) | prompt | llm | output_parser

    return chain