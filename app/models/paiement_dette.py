import uuid

from sqlalchemy import BigInteger, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import SyncBase


class PaiementDette(SyncBase):
    __tablename__ = "paiements_dette_table"

    numero_recu: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
    )

    dette_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("dettes_table.id"),
        nullable=False,
        index=True,
    )

    client_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("clients_table.id"),
        nullable=False,
        index=True,
    )

    montant_usd: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    montant_fc: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    taux_change: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    montant_equivalent_usd: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    mode_paiement: Mapped[str] = mapped_column(
        String(30),
        default="ESPECES_CAISSE",
        nullable=False,
    )

    motif: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )