import os
import faiss
import pickle
from app.utils import load_pdf_text, chunk_text, get_embeddings, get_openai_answer

class RAGPipeline:
    def __init__(self):
        self.index_path = "vectorstore/index.faiss"
        self.data_path = "data/hsc26.pdf"
        self.embeddings_path = "vectorstore/chunks.pkl"

        if os.path.exists(self.index_path) and os.path.exists(self.embeddings_path):
            self.index = faiss.read_index(self.index_path)
            with open(self.embeddings_path, "rb") as f:
                self.chunks = pickle.load(f)
        else:
            text = load_pdf_text(self.data_path)
            self.chunks = chunk_text(text)
            embeddings = get_embeddings(self.chunks)
            self.index = faiss.IndexFlatL2(len(embeddings[0]))
            self.index.add(embeddings)

            faiss.write_index(self.index, self.index_path)
            with open(self.embeddings_path, "wb") as f:
                pickle.dump(self.chunks, f)

    def answer_question(self, query):
        query_emb = get_embeddings([query])[0]
        D, I = self.index.search([query_emb], k=3)
        relevant_chunks = "\n".join([self.chunks[i] for i in I[0]])
        return get_openai_answer(query, relevant_chunks)
