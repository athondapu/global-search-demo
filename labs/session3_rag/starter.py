"""Session 3 starter: chunk, embed and search the training handbook."""

from pathlib import Path

CHUNK_SIZE = 800      # characters
CHUNK_OVERLAP = 100


def chunk_text(text: str, size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP) -> list[str]:
    chunks, start = [], 0
    while start < len(text):
        chunks.append(text[start : start + size])
        start += size - overlap
    return chunks


def load_handbook(path: Path) -> list[str]:
    return chunk_text(path.read_text())


# TODO(trainee): embed the chunks and implement search(query, k=5)
