from langchain.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

def store_chunks_in_chroma(chunks, session_id):
    embeddings = GoogleGenerativeAIEmbeddings(model='models/embedding-001')
    vectorstore = Chroma.from_texts(chunks, embeddings, collection_name=session_id)
    return vectorstore
