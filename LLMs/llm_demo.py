from langchain_openrouter import ChatOpenRouter
from config import settings

llm = ChatOpenRouter(
    model=settings.OPENROUTER_MODEL_1, 
    api_key=settings.OPENROUTER_API_KEY)

result = llm.invoke("which model i am using?")

print(result.content)