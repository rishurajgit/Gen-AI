from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path

current_dir = Path(__file__).parent
pdf_path = current_dir / "something.pdf"

loader = PyPDFLoader(str(pdf_path))

docs = loader.load()

print(docs)

print(len(docs))

print(docs[0].page_content)
print(docs[1].metadata)