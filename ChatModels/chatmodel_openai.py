from langchain_openrouter import ChatOpenRouter
# from dotenv import load_dotenv
# import os
from config import settings

# load_dotenv()

# api_key = os.getenv("OPENAI_API_KEY")
model = ChatOpenRouter(
    model=settings.OPENROUTER_MODEL,
    api_key=settings.OPENROUTER_API_KEY
    )

result = model.invoke("Tell somthing about today")
print(result.content)


# content='The capital of India is **New\u202fDelhi**.' additional_kwargs={'reasoning_content': 'We have a user asking: "What is the captial of India". The user misspells "capital". We need to answer. The capital of India is New Delhi. Provide answer.', 'reasoning_details': [{'type': 'reasoning.text', 'format': 'unknown', 'index': 0, 'text': 'We have a user asking: "What is the captial of India". The user misspells "capital". We need to answer. The capital of India is New Delhi. Provide answer.'}]} response_metadata={'model_name': 'cohere/north-mini-code-20260617:free', 'id': 'gen-1782215635-PZxWGIzNftOTRyzTqWUX', 'created': 1782215635, 'object': 'chat.completion', 'finish_reason': 'stop', 'logprobs': None, 'model_provider': 'openrouter', 'cost': 0.0, 'cost_details': {'upstream_inference_completions_cost': 0.0, 'upstream_inference_prompt_cost': 0.0, 'upstream_inference_cost': 0.0}} id='lc_run--019ef454-6cb5-7d63-89f6-327a66f08b17-0' tool_calls=[] invalid_tool_calls=[] usage_metadata={'input_tokens': 7, 'output_tokens': 48, 'total_tokens': 55, 'input_token_details': {'cache_read': 0, 'cache_creation': 0}, 'output_token_details': {'reasoning': 39}}