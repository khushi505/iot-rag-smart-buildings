# scripts/embed_documents.py

import os
from sentence_transformers import SentenceTransformer
import numpy as np
from chunking import load_and_chunk_documents

# Global in-memory storage
EMBEDDINGS = []
TEXTS = []
METADATAS = []
IDS = []

# Load your model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load and chunk documents from both manuals and specs folders
manual_chunks = load_and_chunk_documents("data/manuals")
# spec_chunks = load_and_chunk_documents("data/specs")
# all_chunks = manual_chunks + spec_chunks

all_chunks = manual_chunks  # For now, only using manuals

# Prepare content and metadata for embedding
texts = [chunk["content"] for chunk in all_chunks]
metadatas = [{"source": chunk["source"]} for chunk in all_chunks]
ids = [chunk["chunk_id"] for chunk in all_chunks]

# Generate embeddings
embeddings = model.encode(texts)

# Store in global lists
EMBEDDINGS.extend(embeddings)
TEXTS.extend(texts)
METADATAS.extend(metadatas)
IDS.extend(ids)

print(f"✅ Successfully embedded and stored {len(texts)} chunks.")

# Save to .npy files for persistence (optional)
np.save("embeddings/embeddings.npy", np.array(EMBEDDINGS))
with open("embeddings/texts.txt", "w", encoding="utf-8") as f:
    for t in TEXTS:
        f.write(t.replace("\n", " ") + "\n")
import json
with open("embeddings/metadatas.json", "w", encoding="utf-8") as f:
    json.dump(METADATAS, f)
with open("embeddings/ids.txt", "w", encoding="utf-8") as f:
    for i in IDS:
        f.write(i + "\n")
