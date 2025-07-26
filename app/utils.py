import os
import re
import openai
import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

openai.api_key = os.getenv("OPENAI_API_KEY")

embed_model = SentenceTransformer("all-MiniLM-L6-v2")


def load_pdf_text(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            raw = page.extract_text()
            if raw:
                text += raw + "\n"
    return text


def chunk_text(text, chunk_size=300):
    sentences = re.split(r'(?<=[।!?\n])', text)
    chunks = []
    current = ""
    for sentence in sentences:
        if len(current) + len(sentence) < chunk_size:
            current += sentence
        else:
            chunks.append(current.strip())
            current = sentence
    if current:
        chunks.append(current.strip())
    return chunks


def get_embeddings(text_chunks):
    return embed_model.encode(text_chunks)


def get_openai_answer(question, context):
    prompt = f"""
    Answer the question based on the following context.

    Context:
    {context}

    Question: {question}
    Answer:
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]
    )
    return response.choices[0].message['content'].strip()
