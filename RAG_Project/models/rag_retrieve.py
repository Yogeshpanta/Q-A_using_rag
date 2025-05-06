from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

from RAG_Project.configs.logging_config import setup_logging
import logging

setup_logging()

class RagImplementation:
    def __init__(self, file):
        self.file = file

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
        # vectorstore =
        return Chroma.from_documents(
            self.split_into_chunks(), embedding_func, persist_directory="./chroma_db"
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

