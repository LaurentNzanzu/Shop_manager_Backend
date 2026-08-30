import uuid

from sqlalchemy import BigInteger, Boolean, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import SyncBase


class LigneFacture(SyncBase):
    __tablename__ = "lignes_facture_table"

    facture_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("factures_table.id"),
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

    devise: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
    )

    quantite: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    prix_unitaire_vente: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    prix_total: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    est_servi: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )