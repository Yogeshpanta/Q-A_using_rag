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
from RAG_Project.models.reranked import Reranker

class TunedChatGeneration:
    def __init__(self, rag_system, model):
        self.rag_system = rag_system
        self.model = model
        self.tokenizer = AutoTokenizer.from_pretrained(model)
        self.reranker = Reranker(self.rag_system)

    def create_pipeline(self):
        pipe = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            max_new_tokens=100,
            temperature=0.7
        )
        return HuggingFacePipeline(pipeline=pipe)

    def define_prompt(self, style="multi_line"):
        if style == "single_lined":
            return ChatPromptTemplate.from_template(RagChatPrompt.SINGLE_LINE_TEMPLATE)
        return ChatPromptTemplate.from_template(RagChatPrompt.PARAGRAPH_TEMPLATE)

    def generate_tuned_output(self, question: str, use_ranked=False):
        retriever = self.rag_system.retrieve_docs()
        llm = self.create_pipeline()
        prompt = self.define_prompt()
        question_answering_chain = create_stuff_documents_chain(llm, prompt)

        if use_ranked:
            docs = self.reranker.rerank(query=question, top_n=3)
            return question_answering_chain.invoke({
                "input": question,
                "context": docs
            })
        else:
            rag_chain = create_retrieval_chain(retriever, question_answering_chain)
            return rag_chain.invoke({"input": question})



# class TunedChatGeneration:
#     def __init__(self, rag_system, model):
#         self.rag_system = rag_system
#         self.model = model
#         self.tokenizer = AutoTokenizer.from_pretrained(model)
#         # self.use_ranked = use_ranked

#     def create_pipeline(self):  # Fixed spelling
#         pipe = pipeline(
#             "text-generation",
#             model=self.model,
#             tokenizer=self.tokenizer,
#             max_new_tokens=100,
#             temperature=0.7
#         )
#         return HuggingFacePipeline(pipeline=pipe)

#     def define_prompt(self, style = "multi_line"):
#         if style == "single_lined":
#             return ChatPromptTemplate.from_template(RagChatPrompt.SINGLE_LINE_TEMPLATE)
#         return ChatPromptTemplate.from_template(RagChatPrompt.PARAGRAPH_TEMPLATE)

#     def generate_tuned_output(self, question: str, use_ranked = True):
#         retriever = self.rag_system.retrieve_docs()
#         llm = self.create_pipeline()
#         prompt = self.define_prompt()
#         # reranked_docs = ReRanked.reranked_docs(query=question, top_n=3)
#         question_answering_chain = create_stuff_documents_chain(llm, prompt)



#         if use_ranked:
#             reranked_docs = self.rag_system.reranked_docs(query=question, top_n=3)
#             docs = [docs for docs in reranked_docs]
#             # rag_chain = create_retrieval_chain(docs, question_answering_chain)
#             # return rag_chain.invoke({"input": question})["answer"]
#             return question_answering_chain.invoke({
#             "input": question,
#             "context": docs
#           })

#         else:
#             question_answering_chain = create_stuff_documents_chain(llm, prompt)
#             rag_chain = create_retrieval_chain(retriever, question_answering_chain)
#             return rag_chain.invoke({"input": question})["answer"]
#         # response= rag_chain.invoke({"input":RagChatPrompt.question})
#         # return response["context"][0].page_content

