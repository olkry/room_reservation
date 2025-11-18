from typing import List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base, CommonMixin


class MeetingRoom(CommonMixin, Base):
    # Имя переговорки должно быть не больше 100 символов,
    # уникальным и непустым.
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=True)

    reservations: Mapped[List['Reservation']] = relationship(cascade='delete')
