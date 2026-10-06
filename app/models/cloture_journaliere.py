from datetime import datetime

from sqlalchemy import BigInteger, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import SyncBase


class ClotureJournaliere(SyncBase):
    __tablename__ = "clotures_journalieres_table"

    date_jour: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        index=True,
    )

    nombre_factures: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    total_ventes_usd: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    total_ventes_fc: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    total_entrees_usd: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    total_entrees_fc: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    total_sorties_usd: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    total_sorties_fc: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    solde_theorique_usd: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    solde_theorique_fc: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    montant_compte_usd: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    montant_compte_fc: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    ecart_usd: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    ecart_fc: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    statut: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    date_validation: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )