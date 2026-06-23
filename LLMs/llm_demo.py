from langchain_openrouter import ChatOpenRouter
from config import settings

llm = ChatOpenRouter(
    model=settings.OPENROUTER_MODEL, 
    api_key=settings.OPENROUTER_API_KEY)

result = llm.invoke("What is the captial of India")

print(result.content)