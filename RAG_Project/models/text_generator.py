from langchain_core.prompts import ChatPromptTemplate
from transformers import AutoTokenizer
from langchain_huggingface import HuggingFacePipeline
from transformers import pipeline
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

import logging
import coloredlogs
from RAG_Project.configs.logging_config import setup_logging

from RAG_Project.prompts.prompt_templates import RagChatPrompt

class TunedChatGeneration:
    def __init__(self, rag_system, model):
        self.rag_system = rag_system
        self.model = model
        self.tokenizer = AutoTokenizer.from_pretrained(model)

    def create_pipeline(self):  # Fixed spelling
        pipe = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            max_new_tokens=100,
            temperature=0.7
        )
        return HuggingFacePipeline(pipeline=pipe)

    def define_prompt(self):
        return ChatPromptTemplate.from_template(RagChatPrompt.SINGLE_LINE_TEMPLATE)

    def generate_tuned_output(self, question: str):
        retriever = self.rag_system.retrieve_docs()
        llm = self.create_pipeline()
        prompt = self.define_prompt()

        question_answering_chain = create_stuff_documents_chain(llm, prompt)
        rag_chain = create_retrieval_chain(retriever, question_answering_chain)

        return rag_chain.invoke({"input": question})["answer"]
        # response= rag_chain.invoke({"input":RagChatPrompt.question})
        # return response["context"][0].page_content