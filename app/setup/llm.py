from langchain_google_genai import ChatGoogleGenerativeAI
import dotenv
import os

dotenv.load_dotenv()

llm = ChatGoogleGenerativeAI(model='gemini-pro', temperature=0.7, api_key=os.getenv("GOOGLE_API_KEY"))