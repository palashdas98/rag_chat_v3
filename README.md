flowchart LR
    A[PDF Upload] --> B[PDF Parser - Docling]
    
    B --> C1[Text Chunks]
    B --> C2[Table Chunks]
    B --> C3[Image Chunks]

    C3 --> D[Vision Language Model]
    D --> C4[Image Summaries]

    C1 --> E[Embedding Model]
    C2 --> E
    C4 --> E

    E --> F[FAISS Vector Store]

    Q[User Query] --> R[Retriever]
    R --> F
    R --> G[Relevant Chunks]

    G --> H[LLM with Custom Prompt]
    H --> I[Grounded Answer + Citations]


    
docker build -t automobile-rag .

docker run -p 8000:8000 --env-file .env automobile-rag