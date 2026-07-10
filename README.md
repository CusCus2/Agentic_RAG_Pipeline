# Agentic RAG Pipeline for Multi-document Question Answering

A lightweight agentic RAG system that routes user queries between direct LLM response and document-grounded retrieval, using Python, LangChain, Chroma, Hugging Face embeddings, and a local language model.

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/CusCus2/Agentic_RAG_Pipeline.git
cd Agentic_RAG_Pipeline
```

### 2. Create and activate a virtual environment
python -m venv .venv

On Windows:

.venv\Scripts\activate

On macOS/Linux:

source .venv/bin/activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Install and run Ollama

This project uses Ollama to run the local language model.

Install Ollama from:

https://ollama.com

Then download the model:

ollama pull llama3

Make sure Ollama is running before starting the API.

### 5. Add PDF documents

Place one or more PDF files inside the documents/ folder.

Example:

documents
- owasp-llm-top-10.pdf
- nist-ai-risk-management-framework.pdf
- secure-ai-guidelines.pdf

### 6. Run the FastAPI server
uvicorn api:app --reload

If successful, the API will be available at:

http://127.0.0.1:8000

### 7. Test the API

Open the interactive FastAPI documentation:

http://127.0.0.1:8000/docs

From there, use the POST /query endpoint and send a request like:

{
  "query": "What are the main risks of LLM applications?"
}

The API returns a structured response containing the original query, the agent decision, generated answer, and retrieved document sources.
