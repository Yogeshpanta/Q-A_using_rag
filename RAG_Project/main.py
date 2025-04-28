# import logging
# from RAG_Project.configs.logging_config import setup_logging
# from RAG_Project.models.rag_retrieve import RagImplementation
# from RAG_Project.models.text_generator import TunedChatGeneration
# import logging
# import coloredlogs
# from RAG_Project.configs.logging_config import setup_logging

# from RAG_Project.routes import rag_routes, rerank_routes
# import uvicorn
# from fastapi import FastAPI

# app = FastAPI(title="Output for retrieve project", description="gives the output when there is no rerank used ")
# app.include_router(rag_routes)

# app = FastAPI(title="putput for rerank", description="gives the output when rerank is True")
# app.include_router(rerank_routes)

# # file_path = "C:/Users/Acer/OneDrive/Desktop/veel_internship_final/transformer.pdf"

# # if __name__ == "__main__":
# #     rag = RagImplementation(file=file_path)
# #     chat_bot = TunedChatGeneration(rag, "gpt2")
# #     print(chat_bot.generate_tuned_output("What is attention in transformers?"))


# if __name__ == "__main__":
#     file_path = "C:/Users/Acer/OneDrive/Desktop/veel_internship_final/transformer.pdf"
#     rag = RagImplementation(file=file_path)
#     chat_bot = TunedChatGeneration(rag, "gpt2")
#     print(chat_bot.generate_tuned_output("What is attention in transformers?"))

#     uvicorn.run(app, host="127.0.0.1", port=8000)
#     # uvicorn.run(app1, host="127.0.0.1", port=8000)


from fastapi import FastAPI
from RAG_Project.routes import rag_routes

app = FastAPI(
    title="RAG System API",
    description="Unified API for RAG system with optional reranking",
)

app.include_router(rag_routes.router, prefix="/api")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
