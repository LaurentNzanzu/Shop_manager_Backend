import uuid
from datetime import datetime
from typing import Optional

from sqlalchemy import Boolean, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import SyncBase


class AuthSession(SyncBase):
    __tablename__ = "sessions_table"

    token: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
    )

    utilisateur_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("utilisateurs_table.id"),
        nullable=False,
        index=True,
    )

    date_debut: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    date_expiration: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    adresse_ip: Mapped[Optional[str]] = mapped_column(
        String(64),
        nullable=True,
    )

    appareil_info: Mapped[Optional[str]] = mapped_column(
        String(255),
        nullable=True,
    )

    est_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )