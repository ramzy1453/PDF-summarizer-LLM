import os
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from app.utils.hash import generate_valid_collection_name
from typing import List
from chromadb import PersistentClient as PersistentChromaClient

persist_directory = "./db"

if not os.path.exists(persist_directory):
    os.makedirs(persist_directory)

embeddings = GoogleGenerativeAIEmbeddings(model='models/embedding-001')

def store_chunks_in_chroma(chunks : List[str] , pdf_id : str) -> Chroma:

    
    vectorstore_exists = load_vectorstore(pdf_id)
    if vectorstore_exists:
        return False
    
    collection_name = generate_valid_collection_name(pdf_id)
    vectorstore = Chroma.from_texts(chunks, 
                                    embeddings, 
                                    collection_name=collection_name, 
                                    persist_directory=persist_directory)

    return True

def load_vectorstore(pdf_id : str) -> Chroma:

    collection_name = generate_valid_collection_name(pdf_id)
    vectorstore = Chroma(collection_name=collection_name, persist_directory=persist_directory, embedding_function=embeddings)

    return vectorstore

def get_uploaded_pdfs() -> List[str]:
    client = PersistentChromaClient(persist_directory)
    collections = client.list_collections()

    return [c.name for c in collections]