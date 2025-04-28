# class RagChatPrompt:

# #   prompt = ChatPromptTemplate.from_messages(
# #     [
# #         (
# #             "system",
# #             (
# #                 "You are a virtual assistant specializing in deep learning. "
# #                 "You should answer questions about the Transformer architecture in deep learning "
# #                 "in a concise, meaningful, and clear way. Use the provided context to inform your answer. "
# #                 "If the context does not contain the answer, say so."
# #             ),
# #         ),
# #         (
# #             "user",
# #             (
# #                 "Context:\n{context}\n\n"
# #                 "Question: {question}"
# #             ),
# #         ),
# #     ]
# # )


class RagChatPrompt:
    SINGLE_LINE_TEMPLATE = """You are an expert assistant. Use the following context to answer the question briefly in one line.

Context:
{context}

Question:
{input}

Answer:"""

    PARAGRAPH_TEMPLATE = """You are an expert assistant. Use the following context to answer the question in a detailed paragraph.

Context:
{context}

Question:
{input}

Answer:"""
