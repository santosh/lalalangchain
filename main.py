from pprint import pprint
from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.tools import create_retriever_tool

load_dotenv()

embeddings = OllamaEmbeddings(model="qwen3-embedding")

texts = [
    'I love apples.',
    'I enjoy oranges.',
    'I think pears taste very good.',
    'I hate bananas.',
    'I dislike raspberries.',
    'I despise mangos.',
    'I love Linux.',
    'I hate Windows.'
]

vector_store = FAISS.from_texts(texts, embeddings)

def main():
    # pprint(vector_store.similarity_search('What fruit does person likes?', k=7))
    # pprint(vector_store.similarity_search('What fruit does person hates?', k=7))

    retriever = vector_store.as_retriever(search_kwargs={"k": 3})

    retriever_tool = create_retriever_tool(
        name="FruitRetriever",
        description="Useful for when you need to answer questions about fruits.",
        retriever=retriever
    )

    agent = create_agent(
        model=ChatOllama(model="qwen3:14b"),
        tools=[retriever_tool],
        system_prompt=(
            "You answer questions about a person's fruit preferences. "
            "Always call the FruitRetriever tool to look up the relevant "
            "statements before answering, and base your answer only on what "
            "it returns."
        ),
    )

    result = agent.invoke(
        {"messages": [{"role": "user", "content": "What fruit does person likes?"}]}
    )

    print("Agent Result:")
    pprint(result["messages"][-1].content)

if __name__ == "__main__":
    main()
