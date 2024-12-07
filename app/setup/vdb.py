import os
from langchain.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from app.utils.hash import generate_valid_collection_name
from typing import List
from chromadb import PersistentClient as PersistentChromaClient

# Répertoire de persistance
persist_directory = "./chroma_data"

# Si le répertoire de persistance n'existe pas, on le crée
if not os.path.exists(persist_directory):
    os.makedirs(persist_directory)

embeddings = GoogleGenerativeAIEmbeddings(model='models/embedding-001')

def store_chunks_in_chroma(chunks : List[str] , session_id : str) -> Chroma:

    
    vectorstore_exists = load_vectorstore(session_id)
    if vectorstore_exists:
        raise Exception("403: PDF already uploaded. Please upload a new PDF file.")
    
    collection_name = generate_valid_collection_name(session_id)
    vectorstore = Chroma.from_texts(chunks, 
                                    embeddings, 
                                    collection_name=collection_name, 
                                    persist_directory=persist_directory)

    return vectorstore

def load_vectorstore(session_id : str) -> Chroma:

    collection_name = generate_valid_collection_name(session_id)
    vectorstore = Chroma(collection_name=collection_name, persist_directory=persist_directory, embedding_function=embeddings)

    return vectorstore

def get_uploaded_pdfs() -> List[str]:
    client = PersistentChromaClient(persist_directory)
    collections = client.list_collections()

    return [c.name for c in collections]