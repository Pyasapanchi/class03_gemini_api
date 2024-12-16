
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv("Gemini-API-key")
llm = GoogleGenerativeAI(model="gemini-1.5-flash",
                         api_key= key,
                         temperature= 0.5)

prompt = llm.invoke("Sing a ballad of LangChain in 2 lines.")
print(prompt)