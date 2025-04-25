
class Reranker:
    def __init__(self, rag_implementation):
        self.rag_system = rag_implementation

    def rerank(self, query, top_n=3):
        vectorstore = self.rag_system.embedding_vectorstore()
        docs_with_scores = vectorstore.similarity_search_with_score(query, k=top_n * 2)
        filtered_sorted = sorted(
            [(doc, score) for doc, score in docs_with_scores],
            key=lambda x: x[1]
        )
        top_docs = [doc for doc, _ in filtered_sorted[:top_n]]
        return top_docs