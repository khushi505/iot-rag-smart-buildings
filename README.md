# IoT Sensor RAG System for Smart Buildings

This project is a lightweight document-aware support system for smart building operations. It allows facility managers to ask questions in natural language and returns relevant context snippets from uploaded building documents using semantic similarity search.
---

## Deployed Link

https://khushi505-iot-rag-smart-buildings-app-68ni6q.streamlit.app/

## Features

- Upload IoT sensor data (.csv)
- Detect anomalies in temperature, humidity, and vibration using IsolationForest
- Retrieve relevant documentation from manuals/specs via embeddings
- Display optimization suggestions based on sensor trends
- GPT-based synthesis of answers from retrieved chunks *(optional)*
- Real-time sensor monitoring via file changes *(optional)*
- User feedback collection via thumbs up/down
- Deployed via Streamlit UI for seamless interaction

---

## Folder Structure

```

iot-rag-smart-buildings/
├── app.py # Main Streamlit interface
├── requirements.txt
├── README.md
│
├── data/
│ ├── sensor_data.csv # Uploaded or simulated sensor readings
│ ├── manuals/ # Maintenance PDFs or TXT files
│ └── specs/ # Building specification docs
│
├── embeddings/
│ └── vector_store/ # ChromaDB persistent directory
│
├── scripts/
│ ├── chunking.py # Splits documents into chunks
│ ├── embed_documents.py # Embeds and stores docs into Chroma
│ ├── retrieve.py # Retrieves top-k matching chunks
│ └── predict_maintenance.py # Detects anomalies in sensor data

```

##  Setup Instructions

### 1. Clone the repo

```
git clone https://github.com/khushi505/iot-rag-smart-buildings.git
cd iot-rag-smart-buildings
```

### 2. Set up Python environment

```
python -m venv venv
venv\Scripts\activate  # Windows
# OR
source venv/bin/activate  # macOS/Linux

pip install -r requirements.txt
```

### 3. Embed documents

```
python scripts/embed_documents.py
```

### 4. Run the app

```
streamlit run app.py
```

## 5. Sample Sensor Data Format

```
timestamp,temperature,humidity,vibration,device_id
2025-08-01T10:00:00,23.4,45,0.01,AC001
2025-08-01T10:05:00,36.1,52,0.03,AC001
...
```

## 6. Demo Photos

<img width="1810" height="723" alt="Screenshot 2025-08-03 155228" src="https://github.com/user-attachments/assets/720ef42c-3434-414d-9ef8-2925d3068856" />


<img width="1843" height="853" alt="Screenshot 2025-08-03 155251" src="https://github.com/user-attachments/assets/c9ad4a7d-111e-4cf6-89ae-66764f97c058" />


<img width="1858" height="444" alt="Screenshot 2025-08-03 155330" src="https://github.com/user-attachments/assets/963ad087-e729-4064-9d31-266a3725e384" />


<img width="1823" height="675" alt="Screenshot 2025-08-03 155338" src="https://github.com/user-attachments/assets/d8d24bbc-7c3b-4f97-a600-2bd2d46530e0" />
