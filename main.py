from RAG_Project.configs.logging_config import setup_logging
import logging
from fastapi import FastAPI
from RAG_Project.routes import rag_routes
import uvicorn
# from routes import rag_routes

setup_logging()

app = FastAPI(
    title="RAG System API",
    description="Unified API for RAG system with optional reranking",
)

app.include_router(rag_routes.router, prefix="/api")

if __name__ == "__main__":
    
    logging.info("Running a FastAPI")
    uvicorn.run(app, host="127.0.0.1", port=8000)
