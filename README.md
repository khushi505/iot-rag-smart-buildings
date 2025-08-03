# IoT Sensor RAG System for Smart Buildings

A Retrieval-Augmented Generation (RAG) system that uses IoT sensor data, maintenance manuals, and building specifications to provide predictive maintenance insights and operational optimization.

---

## Features

- Upload IoT sensor data (.csv)
- Detect anomalies in temperature, humidity, and vibration using IsolationForest
- Retrieve relevant documentation from manuals/specs via embeddings
- Display optimization suggestions based on sensor trends
- GPT-based synthesis of answers from retrieved chunks *(optional)*
- Real-time sensor monitoring via file changes *(optional)*
- User feedback collection via thumbs up/down

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

## Sample Sensor Data Format

```
timestamp,temperature,humidity,vibration,device_id
2025-08-01T10:00:00,23.4,45,0.01,AC001
2025-08-01T10:05:00,36.1,52,0.03,AC001
...
```
