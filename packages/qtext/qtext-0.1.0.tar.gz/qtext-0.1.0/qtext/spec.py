from __future__ import annotations

import struct
from datetime import datetime

import msgspec
import numpy as np


class Record(msgspec.Struct, kw_only=True):
    id: int | str = 0
    text: str
    title: str | None = None
    summary: str | None = None
    vector: list[float] | np.ndarray | None = None
    title_vector: list[float] | np.ndarray | None = None
    sparse_vector: list[float] | np.ndarray | None = None
    score: float = 1.0
    vector_sim: float = 1.0
    title_sim: float = 1.0
    content_bm25: float = 1.0
    title_bm25: float = 1.0
    updated_at: datetime | None = None
    author: str | None = None
    tags: list[str] | None = None
    hidden: bool = False
    boost: float = 1.0

    def use_np(self):
        if isinstance(self.vector, list):
            self.vector = np.array(self.vector)
        if isinstance(self.title_vector, list):
            self.title_vector = np.array(self.title_vector)
        if isinstance(self.sparse_vector, list):
            self.sparse_vector = np.array(self.sparse_vector)

    def simplify(self) -> SimpleRecord:
        return SimpleRecord(
            id=self.id,
            text=self.text,
            title=self.title or "",
        )


class SimpleRecord(msgspec.Struct, kw_only=True):
    id: int | str = 0
    text: str
    title: str


class SparseEmbedding(msgspec.Struct, kw_only=True, frozen=True):
    dim: int
    indices: list[int] = msgspec.field(default_factory=list)
    values: list[float] = msgspec.field(default_factory=list)

    def __post_init__(self):
        if len(self.indices) != len(self.values):
            raise ValueError("indices and values must have the same length")
        if len(set(self.indices)) != len(self.values):
            raise ValueError("indices must be unique")
        if self.indices != sorted(self.indices):
            self.values = [v for _, v in sorted(zip(self.indices, self.values))]
            self.indices.sort()

    def to_str(self) -> str:
        dense = np.zeros(self.dim)
        dense[self.indices] = self.values
        return f"[{','.join(map(str, dense))}]"

    def to_bytes(self) -> bytes:
        return struct.pack(
            f"<II{len(self.indices)}I{len(self.values)}f",
            self.dim,
            len(self.indices),
            *self.indices,
            *self.values,
        )

    @classmethod
    def from_bytes(cls, buf: bytes) -> SparseEmbedding:
        dim = struct.unpack_from("<I", buf)[0]
        length = struct.unpack_from("<I", buf, 4)[0]
        indices = struct.unpack_from(f"<{length}I", buf, 8)
        values = struct.unpack_from(f"<{length}f", buf, 8 + 4 * length)
        return SparseEmbedding(dim=dim, indices=list(indices), values=list(values))


class QueryDocRequest(msgspec.Struct, kw_only=True):
    namespace: str
    query: str
    limit: int = 10
    vector: list[float] | None = None
    sparse_vector: SparseEmbedding | None = None
    metadata: dict | None = None

    def to_record(self) -> Record:
        return Record(
            text=self.query,
            vector=self.vector,
        )


class RetrieveResponse(msgspec.Struct, kw_only=True):
    docs: list[SimpleRecord] = msgspec.field(default_factory=list)
    elapsed: float = 0.0


class RankedResponse(msgspec.Struct, kw_only=True):
    docs: list[SimpleRecord] = msgspec.field(default_factory=list)
    elapsed: float = 0.0
    from_vector: list[int | None] = msgspec.field(default_factory=list)
    from_sparse: list[int | None] = msgspec.field(default_factory=list)
    from_text: list[int | None] = msgspec.field(default_factory=list)

    def fill_hybrid_ids(
        self, vector: RetrieveResponse, sparse: RetrieveResponse, text: RetrieveResponse
    ):
        vector_ids = [doc.id for doc in vector.docs]
        sparse_ids = [doc.id for doc in sparse.docs]
        text_ids = [doc.id for doc in text.docs]
        self.from_vector = [
            vector_ids.index(doc.id) if doc.id in vector_ids else None
            for doc in self.docs
        ]
        self.from_sparse = [
            sparse_ids.index(doc.id) if doc.id in sparse_ids else None
            for doc in self.docs
        ]
        self.from_text = [
            text_ids.index(doc.id) if doc.id in text_ids else None for doc in self.docs
        ]


class QueryExplainResponse(msgspec.Struct, kw_only=True):
    vector: RetrieveResponse = msgspec.field(default_factory=RetrieveResponse)
    sparse: RetrieveResponse = msgspec.field(default_factory=RetrieveResponse)
    text: RetrieveResponse = msgspec.field(default_factory=RetrieveResponse)
    ranked: RankedResponse = msgspec.field(default_factory=RankedResponse)


class AddNamespaceRequest(msgspec.Struct, frozen=True, kw_only=True):
    name: str
    vector_dim: int = 0
    sparse_vector_dim: int = 0


class HighlightRequest(msgspec.Struct, kw_only=True, frozen=True):
    query: str
    docs: list[str]
    threshold: float = 0.8
    ignore_stopwords: bool = True
    template: str = "<mark>{}</mark>"


class HighlightResponse(msgspec.Struct, kw_only=True):
    highlighted: list[str]


class HighlightScore(msgspec.Struct, kw_only=True, frozen=True):
    text: str
    score: float
