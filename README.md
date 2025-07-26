# 📘 Multilingual RAG System (English + Bangla)

This project implements a **Retrieval-Augmented Generation (RAG)** system using FastAPI that answers user questions in **Bengali and English** by retrieving content from a Bengali literature PDF (`HSC26 Bangla 1st Paper`).

---

## 🔧 Setup Guide

### ✅ Prerequisites
- Python 3.9+
- OpenAI API Key
- VS Code or any IDE

### ✅ Installation Steps

```bash
git clone https://github.com/yourusername/rag-system.git
cd rag-system

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt





1. What method or library did you use to extract the text, and why?
Used: PyPDF2
Why: It’s lightweight and supports Bengali fonts reasonably.
Challenges: Some lines and paragraphs are misaligned; preprocessing helps clean this.

2. What chunking strategy did you choose? Why?
Used: Sentence-based chunking with a ~300 character limit
Why: Balances context and avoids loss of meaning, works well with semantic embedding models.

3. What embedding model did you use? Why?
Used: all-MiniLM-L6-v2 from SentenceTransformers
Why: Fast, accurate for semantic tasks, works well with FAISS
Meaning Capture: Captures sentence meaning using transformer architecture.

4. How are you comparing the query with your stored chunks?
Method: Embedding + FAISS + cosine similarity
Why: FAISS is fast and scalable, ideal for semantic search on large document sets.

5. How do you ensure meaningful comparison?
 * Embeddings trained for sentence similarity

 * Query and chunks are in the same embedding space

 * Vague queries will retrieve broader chunks; GPT still tries to summarize


 6. Are the results relevant? If not, what could improve them?
Relevance: Yes, mostly accurate.
Improvements:
 * More accurate chunking (based on headings paragraphs)

 * Use Bangla-specific embedding models

 * Clean and tag text better (speaker, context)

