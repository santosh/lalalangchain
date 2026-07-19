from pprint import pprint
from dotenv import load_dotenv

from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings

load_dotenv()

embeddings = OllamaEmbeddings(model="qwen3-embedding")

texts = [
    'Apple makes very good computers.',
    'I believe Apple is innovative!',
    'I love apples.',
    'I am a fan of MacBooks.',
    'I enjoy oranges.',
    'I like Lenovo ThinkPads.',
    'I think pears taste very good.'
]

vector_store = FAISS.from_texts(texts, embeddings)

def main():
    pprint(vector_store.similarity_search('Apples are my favorite food.', k=7))
    pprint(vector_store.similarity_search('Linux is a great operating system.', k=7))

if __name__ == "__main__":
    main()
