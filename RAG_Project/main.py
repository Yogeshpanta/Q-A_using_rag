import logging
from RAG_Project.configs.logging_config import setup_logging
from RAG_Project.models.rag_retrieve import RagImplementation
from RAG_Project.models.text_generator import TunedChatGeneration
import logging
import coloredlogs
from RAG_Project.configs.logging_config import setup_logging

# file_path = "C:/Users/Acer/OneDrive/Desktop/veel_internship_final/transformer.pdf"

# if __name__ == "__main__":
#     rag = RagImplementation(file=file_path)
#     chat_bot = TunedChatGeneration(rag, "gpt2")
#     print(chat_bot.generate_tuned_output("What is attention in transformers?"))


if __name__ == "__main__":
    file_path = "C:/Users/Acer/OneDrive/Desktop/veel_internship_final/transformer.pdf"
    rag = RagImplementation(file=file_path)
    chat_bot = TunedChatGeneration(rag, "gpt2")
    print(chat_bot.generate_tuned_output("What is attention in transformers?"))
