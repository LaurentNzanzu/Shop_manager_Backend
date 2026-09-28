import uuid
from datetime import datetime
from typing import Optional

from sqlalchemy import BigInteger, Boolean, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import SyncBase


class LigneEmprunt(SyncBase):
    __tablename__ = "lignes_emprunt_table"

    emprunt_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("emprunts_table.id"),
        nullable=False,
        index=True,
    )

    article_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("articles_table.id"),
        nullable=False,
        index=True,
    )

    designation: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    unite_mesure: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
    )

    quantite: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    quantite_retournee: Mapped[int] = mapped_column(
        BigInteger,
        default=0,
        nullable=False,
    )

    est_retourne: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    date_retour_ligne: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    integre_au_stock: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    prix_unitaire_snapshot: Mapped[Optional[int]] = mapped_column(
        BigInteger,
        nullable=True,
    )