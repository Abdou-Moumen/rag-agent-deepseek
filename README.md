# RAG Agent with DeepSeek & Ollama

A simple RAG (Retrieval-Augmented Generation) agent that answers questions based on your PDF documents using a local DeepSeek model.

## 🚀 Features

- Local LLM (no API costs)
- PDF document ingestion
- RAG architecture
- Interactive chat interface
- GPU acceleration support

## 📋 Prerequisites

- Python 3.8+
- Ollama installed
- DeepSeek model pulled

## 🛠️ Installation

### 1. Install Ollama

**Windows/Mac/Linux:**
bash
curl -fsSL https://ollama.com/install.sh | sh

### 2. Pull DeepSeek Model
ollama pull deepseek-r1:1.5b

### 3. Clone Repository
git clone https://github.com/YOUR_USERNAME/rag-agent-deepseek.git
cd rag-agent-deepseek

### 4. Install Python Dependencies
pip install -r requirements.txt

### 5. Add Your PDFs
mkdir data

### Copy your PDF files into the data folder

## Usage
### Start Ollama Server : 
ollama serve
### Run the Agent : 
python rag_agent.py
