# Intelligent Content Processing — Application Code

AI-powered document processing pipeline built with Azure AI services.

## Architecture

```
Document Upload → Blob Storage → Document Intelligence (OCR)
    → AI Foundry Agent Pipeline (Classification → Extraction → Validation)
    → Smart Router → Cosmos DB (ProcessedDocuments / ReviewQueue)
    → Streamlit Dashboard (Process / Results / Review / Analytics)
```

## Quick Start

1. **Copy environment template:**
   ```bash
   cp .env.example .env
   ```

2. **Fill in your Azure credentials** in `.env`

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Authenticate with Azure:**
   ```bash
   az login
   ```

5. **Run the application:**
   ```bash
   streamlit run app.py
   ```

## Files

| File | Description |
|------|-------------|
| `app.py` | Main Streamlit application — UI, pipeline orchestration, routing |
| `doc_processor.py` | Azure AI Document Intelligence SDK integration |
| `cosmos_helper.py` | Cosmos DB dual-container operations (ProcessedDocuments + ReviewQueue) |
| `requirements.txt` | Python dependencies |
| `.env.example` | Environment variable template |
| `Dockerfile` | Container deployment configuration |
| `sample_data/` | Pre-extracted OCR text for testing without Document Intelligence |

## Optional: Docker Deployment

```bash
docker build -t content-processing .
docker run -p 8501:8501 --env-file .env content-processing
```
