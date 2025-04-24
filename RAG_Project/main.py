# import logging
# from RAG_Project.configs.logging_config import setup_logging
from RAG_Project.models.rag_retrieve import RagImplementation
from RAG_Project.models.text_generator import TunedChatGeneration
import logging
import coloredlogs
from RAG_Project.configs.logging_config import setup_logging
# from RAG_Project.experiments.test1 import TunedChatGeneration

file_path = "C:/Users/Acer/OneDrive/Desktop/veel_internship_final/transformer.pdf"


# setup_logging()
# logger = logging.getLogger(__name__)

# # Example usage of logging
# logger.info("This is an info message.")
# logger.warning("This is a warning message.")
# logger.error("This is an error message.")

# import torch
# print(torch.cuda.is_available())
# print(torch.cuda.get_device_name(0) if torch.cuda.is_available() else "No GPU found")
if __name__ == "__main__":
    rag = RagImplementation(file=file_path)
    chat_bot = TunedChatGeneration(rag, "gpt2")
    print(chat_bot.generate_tuned_output("What is attention in transformers?"))
