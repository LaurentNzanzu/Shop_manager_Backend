from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import SyncBase


class Role(SyncBase):
    __tablename__ = "roles_table"

    code: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
    )

    nom: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    description: Mapped[Optional[str]] = mapped_column(
        String(255),
        nullable=True,
    )