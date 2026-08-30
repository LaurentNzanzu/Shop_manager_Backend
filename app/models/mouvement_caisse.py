import uuid
from typing import Optional

from sqlalchemy import BigInteger, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import SyncBase


class MouvementCaisse(SyncBase):
    __tablename__ = "mouvements_caisse_table"

    type: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    montant_usd: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    montant_fc: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    motif: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    source_type: Mapped[Optional[str]] = mapped_column(
        String(50),
        nullable=True,
    )

    source_id: Mapped[Optional[str]] = mapped_column(
        String(100),
        nullable=True,
    )

    client_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("clients_table.id"),
        nullable=True,
        index=True,
    )