# RAG System (English + Bangla)

This project implements a **Retrieval-Augmented Generation (RAG)** system using FastAPI that answers user questions in **Bengali and English** by retrieving content from a Bengali literature PDF (`HSC26 Bangla 1st Paper`).

---

## Setup Guide

### Prerequisites
- Python 3.9+
- OpenAI API Key
- VS Code or any IDE

### Installation Steps

```bash
git clone https://github.com/101rror/RAGsystem.git
cd rag-system
code

create .env file and add OPENAI_API_KEY from https://openai.com/api/
and add it like OPENAI_API_KEY=api


# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
```


## Questions answer

<div class="question">1. What method or library did you use to extract the text, and why?</div>
  <div class="answer">
    <strong>Used:</strong> <code>PyPDF2</code><br>
    <strong>Why:</strong> It’s lightweight and supports Bengali fonts reasonably.<br>
    <strong>Challenges:</strong> Some lines and paragraphs are misaligned; preprocessing helps clean this.
  </div>

  <div class="question">2. What chunking strategy did you choose? Why?</div>
  <div class="answer">
    <strong>Used:</strong> Sentence-based chunking with ~300 character limit<br>
    <strong>Why:</strong> Balances context and avoids loss of meaning, works well with semantic embedding models.
  </div>

  <div class="question">3. What embedding model did you use? Why?</div>
  <div class="answer">
    <strong>Used:</strong> <code>all-MiniLM-L6-v2</code> from SentenceTransformers<br>
    <strong>Why:</strong> Fast, accurate for semantic tasks, works well with FAISS<br>
    <strong>Meaning Capture:</strong> Captures sentence meaning using transformer architecture.
  </div>

  <div class="question">4. How are you comparing the query with your stored chunks?</div>
  <div class="answer">
    <strong>Method:</strong> Embedding + FAISS + cosine similarity<br>
    <strong>Why:</strong> FAISS is fast and scalable, ideal for semantic search on large document sets.
  </div>

  <div class="question">5. How do you ensure meaningful comparison?</div>
  <div class="answer">
    <ul>
      <li>Embeddings trained for sentence similarity</li>
      <li>Query and chunks are in the same embedding space</li>
      <li>Vague queries will retrieve broader chunks; GPT still tries to summarize</li>
    </ul>
  </div>

  <div class="question">6. Are the results relevant? If not, what could improve them?</div>
  <div class="answer">
    <strong>Relevance:</strong> Yes, mostly accurate.<br>
    <strong>Improvements:</strong>
    <ul>
      <li>Improve OCR/text extraction for cleaner input</li>
      <li>Test other embedding models (e.g., multilingual models for Bangla)</li>
      <li>Add prompt engineering or RAG tuning</li>
    </ul>
  </div>
