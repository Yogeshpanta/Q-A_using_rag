
from langchain_core.prompts import ChatPromptTemplate
import logging
import coloredlogs
from RAG_Project.configs.logging_config import setup_logging

class RagChatPrompt:
  
#   prompt = ChatPromptTemplate.from_messages(
#     [
#         (
#             "system",
#             (
#                 "You are a virtual assistant specializing in deep learning. "
#                 "You should answer questions about the Transformer architecture in deep learning "
#                 "in a concise, meaningful, and clear way. Use the provided context to inform your answer. "
#                 "If the context does not contain the answer, say so."
#             ),
#         ),
#         (
#             "user",
#             (
#                 "Context:\n{context}\n\n"
#                 "Question: {question}"
#             ),
#         ),
#     ]
# )

  SINGLE_LINE_TEMPLATE = """You are a Deep Learning expert.You know everything about transformers in Deep Learning. Provide answer in clear,concise, meaningful Use this context:
    {context}

    Answer the question in one line: {input}"""

  MULTI_LINE_TEMPLATE =    """You are a Deep Learning expert and you can give all the answers related to transfromer of Deeplearning.
                            You have to give clear, concise, meaningful answers of the question in maximum of three to four line
                            In the first line ### Give the definitation of the question###
                            In the second line ### Tell why it is important###
                            In the third line ### Descirbe in short in a simple meaning, so that a begineer guy can understand###"""