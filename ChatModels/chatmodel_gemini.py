from langchain_google_genai import ChatGoogleGenerativeAI
from config import settings

llm = ChatGoogleGenerativeAI(
    model=settings.GEMINI_CHAT_MODEL,
    google_api_key=settings.GEMINI_API_KEY
)

result = llm.invoke("What is the captial of India?")

print(result.content)