from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import SyncBase


class Categorie(SyncBase):
    __tablename__ = "categories_table"

    code: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
    )

    designation: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    description: Mapped[Optional[str]] = mapped_column(
        String(255),
        nullable=True,
    )

    devise: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
    )