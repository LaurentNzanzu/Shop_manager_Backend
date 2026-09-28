import uuid
from datetime import datetime
from typing import Optional

from sqlalchemy import BigInteger, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import SyncBase


class Dette(SyncBase):
    __tablename__ = "dettes_table"

    numero_dette: Mapped[str] = mapped_column(
        String(100),
        default="",
        nullable=False,
    )

    client_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("clients_table.id"),
        nullable=False,
        index=True,
    )

    facture_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("factures_table.id"),
        nullable=True,
        index=True,
    )

    origine: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    statut: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    montant_initial_usd: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    montant_paye_usd: Mapped[int] = mapped_column(
        BigInteger,
        default=0,
        nullable=False,
    )

    montant_restant_usd: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    montant_initial_fc: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    montant_restant_fc: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    taux_change: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    date_echeance: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    date_rappel_prevue: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    date_derniere_alerte: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )