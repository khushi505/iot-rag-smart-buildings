# app.py – Streamlit UI

import streamlit as st
import pandas as pd
from scripts.predict_maintenance import load_sensor_data, detect_anomalies
from scripts.retrieve import retrieve_relevant_chunks, add_documents

# --- Add these lines to load and embed documents at startup ---
from scripts.chunking import load_and_chunk_documents  # Adjust import if needed

@st.cache_resource(show_spinner="Loading and embedding documents...")
def initialize_embeddings():
    # Load and chunk documents from both manuals and specs folders
    manual_chunks = load_and_chunk_documents("data/manuals")
    # spec_chunks = load_and_chunk_documents("data/specs")
    # all_chunks = manual_chunks + spec_chunks

    all_chunks = manual_chunks  # For now, only using manuals

    texts = [chunk["content"] for chunk in all_chunks]
    metadatas = [{"source": chunk["source"]} for chunk in all_chunks]
    ids = [chunk["chunk_id"] for chunk in all_chunks]

    add_documents(texts, metadatas, ids)

initialize_embeddings()
# --- End embedding initialization ---

st.set_page_config(page_title="Smart Building RAG Assistant", layout="wide")
st.title("🏢 IoT Sensor RAG Assistant for Smart Buildings")

# --- Sensor Upload & Anomaly Detection ---
st.header("📊 Upload IoT Sensor Data")
uploaded_file = st.file_uploader("Upload sensor_data.csv", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df = detect_anomalies(df)

    st.subheader("🔍 Sensor Data Overview")
    st.dataframe(df.tail(10))

    st.subheader("⚠️ Detected Anomalies")
    anomalies = df[df["is_anomaly"]]
    if anomalies.empty:
        st.success("No anomalies detected.")
    else:
        st.error(f"{len(anomalies)} anomalies found!")
        st.dataframe(anomalies)

    # --- Optimization Recommendations ---
    st.subheader("💡 Optimization Suggestions")
    suggestions = []
    if df["temperature"].mean() > 30:
        suggestions.append("Consider optimizing HVAC settings for energy efficiency.")
    if df["humidity"].mean() > 60:
        suggestions.append("High humidity detected. Inspect dehumidifiers or ventilation systems.")
    if df["vibration"].max() > 0.15:
        suggestions.append("Unusual vibration levels. Check motor balance or loose components.")

    if suggestions:
        for s in suggestions:
            st.markdown(f"- {s}")
    else:
        st.markdown("✅ No optimization actions suggested at this time.")

# --- Query Section ---
st.header("📚 Ask a Maintenance Question")
query = st.text_input("Enter your question about the system, issue, or maintenance:")

if st.button("🔎 Retrieve Info") and query:
    with st.spinner("Searching documents..."):
        results = retrieve_relevant_chunks(query)

    st.subheader("📄 Relevant Context")
    if results:
        for i, (doc, meta) in enumerate(results):
            st.markdown(f"**{i+1}. Source: `{meta['source']}`**")
            st.markdown(f"> {doc}\n")

        # --- CSAT Feedback ---
        st.subheader("📝 Was this helpful?")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("👍 Yes"):
                st.success("Thank you for your feedback!")
        with col2:
            if st.button("👎 No"):
                st.warning("We’ll use your feedback to improve the assistant.")

    else:
        st.warning("No relevant information found. Try rephrasing your question or ensure documents are embedded.")
