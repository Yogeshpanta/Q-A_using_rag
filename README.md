RAG Project
A modern, modular Retrieval-Augmented Generation (RAG) system built with FastAPI, HuggingFace Transformers, LangChain, and ChromaDB. This project provides a unified API for document retrieval, reranking, and context-aware text generation, supporting both standard and reranked RAG pipelines.

Features
Document Ingestion: Load and chunk PDF documents for retrieval.

Embedding & Vector Store: Uses Sentence Transformers and ChromaDB for efficient semantic search.

Retrieval-Augmented Generation: Integrates a retriever with a language model for context-aware answers.

Optional Reranking: Supports reranking of retrieved documents to improve answer relevance.

API-First: FastAPI endpoints for querying with or without reranking.

Customizable Prompts: Choose between concise (single-line) and detailed (paragraph) answer styles.

Extensible: Modular design for easy integration of new models or retrieval strategies.

Installation
Prerequisites
Python 3.11 or higher

Clone the Repository
git clone git@github.com:Yogeshpanta/Q-A_using_rag.git

Activate the enviornment
.venv/Scripts/activate
Install Dependencies
uv sync

Usage
1. Prepare Your Document
Place the PDF document you want to use for retrieval at the specified path in your configuration (default: C:/Users/Acer/OneDrive/Desktop/veel_internship_final/transformer.pdf)

2. Start the API Server

uvicorn RAG_Project.main:app --reload
or 
uv run ./RAG_Project/main.py

3. Query the API
Send a POST request to /api/query with a question. You can optionally enable reranking

Core Components
RagImplementation: Handles file reading, chunking, embedding, and retrieval.
Reranker : Handles reranking if used_rerank = True
TunedChatGeneration: Manages prompt selection, pipeline creation, and answer generation (with or without reranking).
API Router: Exposes /api/query endpoint for unified querying.

Configuration
Model: Default is "gpt2", but can be changed in the code or via environment/config.
Embeddings: Uses "sentence-transformers/all-MiniLM-L6-v2".
Vector Store: ChromaDB, persisted at ./chroma_db.
Chunk Size: 512 characters with 50 overlap (configurable in RagImplementation).

Development
Run Tests
Add your tests in a tests/ directory and run with your preferred test runner.

Dependencies
Key dependencies include:

fastapi
uvicorn
chromadb
langchain-huggingface
transformers
sentence-transformers
pypdf
torch
pydantic
colorlog, coloredlogs (for logging)
rank-llm (for reranking)
See pyproject.toml for the full list.

Acknowledgments
HuggingFace Transformers
LangChain
ChromaDB
FastAPI




