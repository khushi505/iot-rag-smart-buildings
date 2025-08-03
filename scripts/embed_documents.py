# scripts/embed_documents.py

import os
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.utils import embedding_functions
from chunking import load_and_chunk_documents

# Load your model (you can use 'all-MiniLM-L6-v2' or any other suitable one)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Initialize Chroma client and collection
chroma_client = chromadb.PersistentClient(path="embeddings/vector_store")

collection = chroma_client.get_or_create_collection(name="smart_building_docs")

# Load and chunk documents from both manuals and specs folders
manual_chunks = load_and_chunk_documents("data/manuals")
spec_chunks = load_and_chunk_documents("data/specs")
all_chunks = manual_chunks + spec_chunks

# Prepare content and metadata for embedding
texts = [chunk["content"] for chunk in all_chunks]
metadatas = [{"source": chunk["source"]} for chunk in all_chunks]
ids = [chunk["chunk_id"] for chunk in all_chunks]

# Generate embeddings
embeddings = model.encode(texts).tolist()

# Store in Chroma
collection.add(
    documents=texts,
    embeddings=embeddings,
    metadatas=metadatas,
    ids=ids
)

print(f"✅ Successfully embedded and stored {len(texts)} chunks.")
