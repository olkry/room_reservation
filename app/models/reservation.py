from datetime import datetime

from sqlalchemy import DateTime, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base, CommonMixin


class Reservation(CommonMixin, Base):
    from_reserve: Mapped[datetime] = mapped_column(DateTime)
    to_reserve: Mapped[datetime] = mapped_column(DateTime)
    meetingroom_id: Mapped[int] = mapped_column(Integer,
                                                ForeignKey('meetingroom.id'))

    def __repr__(self):
        return (
            f'Забронировано с {self.from_reserve} по {self.to_reserve}'
        )
