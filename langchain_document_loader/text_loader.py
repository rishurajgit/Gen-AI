from pathlib import Path
from langchain_community.document_loaders import TextLoader

# Get the folder where this Python file is located
current_dir = Path(__file__).parent

# Build the full path to cricket.txt
file_path = current_dir / "cricket.txt"

loader = TextLoader(str(file_path), encoding="utf-8")

docs = loader.load() 

print(docs)
print(len(docs))

print(docs[0])