# Use Python 3.10 with latest SQLite support
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the full app code
COPY . .

# Streamlit environment setup
ENV PYTHONUNBUFFERED=1
ENV STREAMLIT_PORT=7860

# Expose default port
EXPOSE 7860

# Launch Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.address=0.0.0.0"]
