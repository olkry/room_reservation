from datetime import datetime, timedelta

from pydantic import (
    BaseModel, ConfigDict, Field, field_validator, model_validator
)
from typing_extensions import Self

# Представить объект datetime в виде строки с точностью до минут.
FROM_TIME = (
    datetime.now() + timedelta(minutes=10)
).isoformat(timespec='minutes')

TO_TIME = (
    datetime.now() + timedelta(hours=1)
).isoformat(timespec='minutes')


class ReservationBase(BaseModel):
    from_reserve: datetime = Field(..., examples=[FROM_TIME])
    to_reserve: datetime = Field(..., examples=[TO_TIME])

    model_config = ConfigDict(
        extra='forbid',
        # json_schema_extra={
        #     'example': {
        #         'from_time': '2028-04-24T11:00',
        #         'to_time': '2028-04-24T12:00'
        #     }
        # }
    )


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
