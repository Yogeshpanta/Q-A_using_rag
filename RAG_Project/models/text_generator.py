from langchain_core.prompts import ChatPromptTemplate
# from transformers import AutoTokenizer
# from langchain_huggingface import HuggingFacePipeline
# from transformers import pipeline
from langchain.chains.combine_documents import create_stuff_documents_chain
# from langchain.chains import create_retrieval_chain


from RAG_Project.prompts.prompt_templates import RagChatPrompt
from RAG_Project.configs.logging_config import setup_logging
import logging
from RAG_Project.models.reranked import Reranker
# from langchain_core.documents import Document

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
setup_logging()
openai_api_key = os.getenv("OPENAI_API_KEY")


# Using openai
class TunedChatGeneration:
    def __init__(self, rag_system,style):
        self.rag_system = rag_system
        # self.model = model
        # self.tokenizer = AutoTokenizer.from_pretrained(model)
        self.style = style
        self.reranker = Reranker(self.rag_system)

    def define_prompt(self):
        if self.style == "single_line":
            return ChatPromptTemplate.from_template(RagChatPrompt.SINGLE_LINE_TEMPLATE)
        return ChatPromptTemplate.from_template(RagChatPrompt.PARAGRAPH_TEMPLATE)

    def generate_tuned_output(self, question: str):
        # retriever = self.rag_system.retrieve_docs()
        llm = ChatOpenAI(model="gpt-4o-mini", api_key=openai_api_key)
        prompt = self.define_prompt()
        question_answering_chain = create_stuff_documents_chain(llm, prompt)

        # if use_ranked:
        docs = self.reranker.rerank(query=question, top_n=3)
        result =  question_answering_chain.invoke({"input": question, "context": docs})
        # return {
        #         "question":question,
        #         "answer":result
        #     }
        logging.info("Generated result based on prompt, query and llm")
        return result