import os
import fitz  
from typing import List

def load_text_from_pdf(pdf_path: str) -> str:
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def load_text_from_txt(txt_path: str) -> str:
    with open(txt_path, 'r', encoding='utf-8') as file:
        return file.read()

def split_text_into_chunks(text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = words[i:i + chunk_size]
        chunks.append(" ".join(chunk))
    return chunks

def load_and_chunk_documents(directory: str) -> List[dict]:
    chunks = []
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if filename.endswith(".pdf"):
            text = load_text_from_pdf(file_path)
        elif filename.endswith(".txt"):
            text = load_text_from_txt(file_path)
        else:
            continue

        doc_chunks = split_text_into_chunks(text)
        for i, chunk in enumerate(doc_chunks):
            chunks.append({
                "content": chunk,
                "source": filename,
                "chunk_id": f"{filename}_chunk_{i}"
            })
    return chunks
