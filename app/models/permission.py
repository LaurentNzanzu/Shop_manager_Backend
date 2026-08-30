from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import SyncBase


class Permission(SyncBase):
    __tablename__ = "permissions_table"

    code: Mapped[str] = mapped_column(
        String(150),
        unique=True,
        nullable=False,
    )

    libelle: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    module: Mapped[Optional[str]] = mapped_column(
        String(100),
        nullable=True,
    )