from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

from RAG_Project.configs.logging_config import setup_logging
import logging
import os

setup_logging()

# class RagImplementation:
#     def __init__(self, file):
#         self.file = file

#     def file_reader(self):
#         loader = PyPDFLoader(self.file)
#         docs = loader.load()
#         return docs

#     def split_into_chunks(self):
#         splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=50)
#         document = self.file_reader()
#         splitted_text = splitter.split_documents(document)
#         return splitted_text

#     def embedding_vectorstore(self):
#         embedding_func = HuggingFaceEmbeddings(
#             model_name="sentence-transformers/all-MiniLM-L6-v2"
#         )
#         # vectorstore =
#         return Chroma.from_documents(
#             self.split_into_chunks(), embedding_func, persist_directory="./chroma_db"
#         )

#     def retrieve_docs(self):
#         # shutil.rmtree("./chroma_db", ignore_errors=True)
#         embedded_store_text = self.embedding_vectorstore()
#         retriever = embedded_store_text.as_retriever(
#             search_type="similarity_score_threshold",
#             search_kwargs={"k": 3, "score_threshold": 0.25},
#         )
#         # ans = retriever.invoke("What is Transformer?")
#         # return ans
#         logging.info("Generated retriever")
#         return retriever

import os
from dotenv import load_dotenv
load_dotenv()

pdf_path = os.getenv("PDF_PATH")

class RagImplementation:
    # def __init__(self, file):
    def __init__(self):
        self.file = pdf_path

    def file_reader(self):
        loader = PyPDFLoader(self.file)
        docs = loader.load()
        return docs

    def split_into_chunks(self):
        splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=50)
        document = self.file_reader()
        splitted_text = splitter.split_documents(document)
        return splitted_text

    def embedding_vectorstore(self):
        embedding_func = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        persist_path = "./chroma_db"

        if os.path.exists(persist_path):
            logging.info("Chroma DB already exists. Loading existing vectorstore.")
            return Chroma(
                persist_directory=persist_path,
                embedding_function=embedding_func
        )
        else:
            logging.info("Chroma DB not found. Creating new embeddings and vectorstore.")
            return Chroma.from_documents(
                self.split_into_chunks(),
                embedding_func,
                persist_directory=persist_path
            )
            

    def retrieve_docs(self):
        # shutil.rmtree("./chroma_db", ignore_errors=True)
        embedded_store_text = self.embedding_vectorstore()
        retriever = embedded_store_text.as_retriever(
            search_type="similarity_score_threshold",
            search_kwargs={"k": 3, "score_threshold": 0.25},
        )
        # ans = retriever.invoke("What is Transformer?")
        # return ans
        logging.info("Generated retriever")
        return retriever

