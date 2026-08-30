from typing import Optional

from sqlalchemy import BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import SyncBase


class ParametresBoutique(SyncBase):
    __tablename__ = "parametres_boutique_table"

    nom_boutique: Mapped[Optional[str]] = mapped_column(
        String(255),
        nullable=True,
    )

    logo_file_name: Mapped[Optional[str]] = mapped_column(
        String(255),
        nullable=True,
    )

    numero_impot: Mapped[Optional[str]] = mapped_column(
        String(100),
        nullable=True,
    )

    numero_rccm: Mapped[Optional[str]] = mapped_column(
        String(100),
        nullable=True,
    )

    telephone: Mapped[Optional[str]] = mapped_column(
        String(50),
        nullable=True,
    )

    email: Mapped[Optional[str]] = mapped_column(
        String(255),
        nullable=True,
    )

    adresse: Mapped[Optional[str]] = mapped_column(
        String(255),
        nullable=True,
    )

    heure_ouverture: Mapped[Optional[str]] = mapped_column(
        String(50),
        nullable=True,
    )

    heure_fermeture: Mapped[Optional[str]] = mapped_column(
        String(50),
        nullable=True,
    )

    taux_change_defaut: Mapped[int] = mapped_column(
        BigInteger,
        default=28000000,
        nullable=False,
    )