# scripts/retrieve.py

from sentence_transformers import SentenceTransformer
import numpy as np

# Global in-memory storage (populated at runtime)
EMBEDDINGS = []
TEXTS = []
METADATAS = []
IDS = []

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

def add_documents(texts, metadatas, ids):
    """Call this function at startup to add documents to memory."""
    global EMBEDDINGS, TEXTS, METADATAS, IDS
    embeddings = model.encode(texts)
    EMBEDDINGS.extend(embeddings)
    TEXTS.extend(texts)
    METADATAS.extend(metadatas)
    IDS.extend(ids)

def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def retrieve_relevant_chunks(query: str, top_k: int = 5):
    if not EMBEDDINGS:
        return []
    query_embedding = model.encode([query])[0]
    similarities = [cosine_similarity(query_embedding, emb) for emb in EMBEDDINGS]
    top_indices = np.argsort(similarities)[-top_k:][::-1]
    results = []
    for idx in top_indices:
        results.append((TEXTS[idx], METADATAS[idx]))
    return results

# Example usage: populate memory at startup
if __name__ == "__main__":
    # Example: Replace with your actual chunk loading logic
    texts = ["How to reset the HVAC system?", "Check the humidity sensor regularly."]
    metadatas = [{"source": "manual1.pdf"}, {"source": "specs1.pdf"}]
    ids = ["chunk1", "chunk2"]
    add_documents(texts, metadatas, ids)

    query = input("🔍 Enter your maintenance or sensor-related query: ")
    chunks = retrieve_relevant_chunks(query)
    for i, (doc, meta) in enumerate(chunks):
        print(f"\n🔹 Result {i+1} (Source: {meta['source']}):\n{doc}")
