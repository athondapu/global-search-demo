# Session 3: RAG lab

Build a small retrieval-augmented generation pipeline over the training handbook.

1. Chunk the handbook (`starter.py` uses fixed-size chunks with overlap).
2. Embed each chunk with a local sentence-transformers model.
3. Store the vectors and search them by cosine similarity.
4. Answer a question using the top results, citing each chunk.

You need a seat in the shared lab environment: run `uv run lab seat --cohort <your cohort>`
before the session.

**Stretch:** try a smaller chunk size and compare answer quality on the five sample questions.
