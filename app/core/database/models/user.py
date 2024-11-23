from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from .model import Model


class User(Model):
    __tablename__ = "Users"

    id: Mapped[int] = mapped_column(
        Integer(),
        primary_key=True,
        nullable=False,
        autoincrement=True,
    )
    first_name: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
    )
    last_name: Mapped[str] = mapped_column(
        String(64),
        nullable=True,
    )

    def __init__(
        self,
        *,
        first_name: str,
        last_name: str,
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name

    @property
    def display_name(self) -> str:
        return f"{self.first_name} {self.last_name or ""}".strip()

    def __repr__(self) -> str:
        return f"<{type(self).__name__} {self.display_name}>"
