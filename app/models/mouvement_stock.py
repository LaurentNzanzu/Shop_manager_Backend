import uuid
from typing import Optional

from sqlalchemy import BigInteger, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import SyncBase


class MouvementStock(SyncBase):
    __tablename__ = "mouvements_stock_table"

    article_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("articles_table.id"),
        nullable=False,
        index=True,
    )

    type: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    quantite: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    unite_mesure: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
    )

    avant_mouvement: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    apres_mouvement: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    prix_unitaire: Mapped[Optional[int]] = mapped_column(
        BigInteger,
        nullable=True,
    )

    motif: Mapped[Optional[str]] = mapped_column(
        String(255),
        nullable=True,
    )

    source_type: Mapped[Optional[str]] = mapped_column(
        String(50),
        nullable=True,
    )

    source_id: Mapped[Optional[str]] = mapped_column(
        String(100),
        nullable=True,
    )