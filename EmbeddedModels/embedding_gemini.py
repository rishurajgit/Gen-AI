from langchain_google_genai import GoogleGenerativeAIEmbeddings
from config import settings

embedding_model = GoogleGenerativeAIEmbeddings(
    model = settings.GEMINI_EMBEDDING_MODEL,
    google_api_key = settings.GEMINI_API_KEY,
    dimension = 32
)

result = embedding_model.embed_query(
    "Delhi is the capital of India"
)
print(str(result))