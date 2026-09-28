import uuid

from sqlalchemy import BigInteger, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import SyncBase


class Facture(SyncBase):
    __tablename__ = "factures_table"

    numero_facture: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
    )

    client_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("clients_table.id"),
        nullable=False,
        index=True,
    )

    taux_change: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    type_facture: Mapped[str] = mapped_column(
        String(20),
        default="VENTE",
        nullable=False,
    )

    montant_total_usd: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    montant_total_fc: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    montant_paye_usd: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    montant_paye_fc: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    statut_paiement: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    statut_service: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )