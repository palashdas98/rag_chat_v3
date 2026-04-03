import faiss
import numpy as np

index = faiss.IndexFlatL2(768)
documents = []
metadatas = []

def add_to_index(embeddings, chunks, metadata):
    index.add(np.array(embeddings).astype("float32"))
    documents.extend(chunks)
    metadatas.extend(metadata)

def retrieve(query_embedding, k=5):
    _, idxs = index.search(np.array([query_embedding]).astype("float32"), k)
    return [(documents[i], metadatas[i]) for i in idxs[0]]

