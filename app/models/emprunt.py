import uuid
from datetime import datetime
from typing import Optional

from sqlalchemy import DateTime, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import SyncBase


class Emprunt(SyncBase):
    __tablename__ = "emprunts_table"

    numero_emprunt: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
    )

    type: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
    )

    nom_personne: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    contact_personne: Mapped[Optional[str]] = mapped_column(
        String(50),
        nullable=True,
    )

    date_emprunt: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    date_retour_prevue: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    date_retour_effective: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    statut: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    motif: Mapped[Optional[str]] = mapped_column(
        String(255),
        nullable=True,
    )

    date_derniere_alerte: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )