from datetime import datetime

from pydantic import BaseModel, ConfigDict, model_validator, field_validator
from typing_extensions import Self


class ReservationBase(BaseModel):
    from_reserve: datetime
    to_reserve: datetime


class ReservationUpdate(ReservationBase):
    @field_validator('from_reserve')
    @classmethod
    def check_from_reserve_later_than_now(cls, value):
        if value <= datetime.now():
            error = (
                'Время начала бронирования '
                'не может быть меньше текущего времени'
            )
            raise ValueError(error)
        return value

    @model_validator(mode='after')
    def check_from_reserve_before_to_reserve(self) -> Self:
        if self.from_reserve >= self.to_reserve:
            error = (
                'Время начала бронирования '
                'не может быть больше времени окончания'
            )
            raise ValueError(error)
        return self


class ReservationCreate(ReservationUpdate):
    meetingroom_id: int


class ReservationDB(ReservationBase):
    id: int
    meetingroom_id: int

    model_config = ConfigDict(from_attributes=True)
