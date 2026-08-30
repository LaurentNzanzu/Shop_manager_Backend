import uuid
from datetime import datetime
from typing import Optional

from sqlalchemy import BigInteger, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import SyncBase


class Article(SyncBase):
    __tablename__ = "articles_table"

    code_inventaire: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
    )

    designation: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True,
    )

    categorie_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("categories_table.id"),
        nullable=False,
        index=True,
    )

    unite_mesure: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
    )

    prix_achat: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    prix_vente: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    seuil_alerte: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    quantite_actuelle: Mapped[int] = mapped_column(
        BigInteger,
        default=0,
        nullable=False,
    )

    date_enregistrement: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    date_expiration: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )