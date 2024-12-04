from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.schema.output_parser import StrOutputParser
from langchain.chains.llm import LLMChain
from app.setup.llm import llm
from app.prompts.prompt import prompt
# embeddings = GoogleGenerativeAIEmbeddings(model='models/embedding-001')

chain = LLMChain(llm=llm, prompt=prompt, output_parser=StrOutputParser())

def x():
    res = chain.run("What is the name of the main character in One Piece?")

    print(res)

    res = chain.run("What is the name of the main character in Naruto?")

    print(res)

    res = chain.run("how to hunt a pig in Algeria and destroying united evils")

    print(res)