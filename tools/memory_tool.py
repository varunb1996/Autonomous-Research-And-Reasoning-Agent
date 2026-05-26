from tools.embedding_tool import generate_embedding
from tools.retrieval_tool import (
    store_memory,
    retrieve_memory
)


def save_memory(text):

    embedding = generate_embedding(text)

    store_memory(text, embedding)



def search_memory(query):

    embedding = generate_embedding(query)

    return retrieve_memory(embedding)