import uuid
from datetime import datetime
from typing import Optional

from sqlalchemy import Boolean, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import SyncBase


class Utilisateur(SyncBase):
    __tablename__ = "utilisateurs_table"

    nom_complet: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    username: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
    )

    email: Mapped[Optional[str]] = mapped_column(
        String(255),
        nullable=True,
    )

    telephone: Mapped[Optional[str]] = mapped_column(
        String(50),
        nullable=True,
    )

    mot_de_passe_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    langue_preferee: Mapped[str] = mapped_column(
        String(10),
        default="fr",
        nullable=False,
    )

    est_actif: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    role_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("roles_table.id"),
        nullable=False,
        index=True,
    )

    derniere_connexion: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )