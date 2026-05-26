from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct
)

import uuid

COLLECTION_NAME = "agent_memory"

client = QdrantClient(
    path="memory/qdrant_storage"
)

collections = client.get_collections().collections

collection_names = [
    c.name for c in collections
]

if COLLECTION_NAME not in collection_names:

    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(
            size=384,
            distance=Distance.COSINE
        )
    )


def store_memory(text, embedding):

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=[
            PointStruct(
                id=str(uuid.uuid4()),
                vector=embedding,
                payload={
                    "text": text
                }
            )
        ]
    )


def retrieve_memory(query_embedding):

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_embedding,
        limit=5
    )

    memories = []

    for point in results.points:

        memories.append(
            point.payload["text"]
        )

    return memories