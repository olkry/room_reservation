from typing import Optional

from pydantic import BaseModel, Field, ConfigDict, field_validator


class MeetingRoomBase(BaseModel):
    name: Optional[str] = Field(
        None, min_length=1, max_length=100, title='Название')
    description: Optional[str] = None


class MeetingRoomCreate(MeetingRoomBase):
    name: str = Field(min_length=1, max_length=100)


class MeetingRoomDB(MeetingRoomBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class MeetingRoomUpdate(MeetingRoomBase):
    @field_validator('name')
    @classmethod
    def name_cannot_be_null(cls, value):
        if value is None:
            error = 'Имя переговорки не может быть пустым!'
            raise ValueError(error)
        return value
