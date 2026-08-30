from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import SyncBase


class Client(SyncBase):
    __tablename__ = "clients_table"

    nom_complet: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    telephone: Mapped[Optional[str]] = mapped_column(
        String(50),
        nullable=True,
    )