# class TunedChatGeneration:
#     def __init__(self, rag_system, model, style):
#         self.rag_system = rag_system
#         self.model = model
#         self.tokenizer = AutoTokenizer.from_pretrained(model)
#         self.style = style
#         self.reranker = Reranker(self.rag_system)

#     def create_pipeline(self):
#         pipe = pipeline(
#             "text-generation",
#             model=self.model,
#             tokenizer=self.tokenizer,
#             max_new_tokens=100,
#             temperature=0.7,
#         )
#         return HuggingFacePipeline(pipeline=pipe)

#     def define_prompt(self):
#         if self.style == "single_line":
#             return ChatPromptTemplate.from_template(RagChatPrompt.SINGLE_LINE_TEMPLATE)
#         return ChatPromptTemplate.from_template(RagChatPrompt.PARAGRAPH_TEMPLATE)

#     def generate_tuned_output(self, question: str):
#         # retriever = self.rag_system.retrieve_docs()
#         llm = self.create_pipeline()
#         prompt = self.define_prompt()
#         question_answering_chain = create_stuff_documents_chain(llm, prompt)

#         # if use_ranked:
#         docs = self.reranker.rerank(query=question, top_n=3)
#         result =  question_answering_chain.invoke({"input": question, "context": docs})
#         return {
#                 "question":question,
#                 "answer":result
#             }
        # else:
        #     retriever = self.rag_system.retrieve_docs()
        #     docs = retriever.invoke(question)
            
        #     # extract only page_content
        #     clean_docs = [doc.page_content for doc in docs]
            
        #     # wrap in Document objects with only page_content
        #     clean_docs_wrapped = [Document(page_content=page) for page in clean_docs]

        #     result =  question_answering_chain.invoke({"input": question, "context": clean_docs_wrapped})
        #     return {
        #         "question": question,
        #         "result":result
        #     }