from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from config import settings

llm = HuggingFaceEndpoint(
    repo_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',
    huggingfacehub_api_token=settings.HUGGINGFACEHUB_API_TOKEN
)


model = ChatHuggingFace(llm=llm)


result = model.invoke("What is the capital of india?")

print(result.content)