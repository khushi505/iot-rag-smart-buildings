# scripts/retrieve.py

from sentence_transformers import SentenceTransformer
import chromadb

# Load same embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Connect to ChromaDB collection
chroma_client = chromadb.PersistentClient(path="embeddings/vector_store")

collection = chroma_client.get_or_create_collection(name="smart_building_docs")

def retrieve_relevant_chunks(query: str, top_k: int = 5):
    query_embedding = model.encode(query).tolist()
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )
    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]
    return list(zip(documents, metadatas))

if __name__ == "__main__":
    query = input("🔍 Enter your maintenance or sensor-related query: ")
    chunks = retrieve_relevant_chunks(query)
    for i, (doc, meta) in enumerate(chunks):
        print(f"\n🔹 Result {i+1} (Source: {meta['source']}):\n{doc}")
