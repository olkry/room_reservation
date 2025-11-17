from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.encoders import jsonable_encoder

from app.models.meeting_room import MeetingRoom
from app.schemas.meeting_room import MeetingRoomCreate, MeetingRoomUpdate


async def create_meeting_room(
        new_room: MeetingRoomCreate,
        session: AsyncSession,
) -> MeetingRoom:
    # Конвертируем объект MeetingRoomCreate в словарь.
    new_room_data = new_room.model_dump()
    db_room = MeetingRoom(**new_room_data)

    session.add(db_room)
    # Записываем изменения непосредственно в БД.
    # Так как сессия асинхронная, используем ключевое слово await.
    await session.commit()
    # await session.refresh(db_room)
    return db_room


async def get_room_id_by_name(
        room_name: str,
        session: AsyncSession,
) -> Optional[int]:

    db_room_id = await session.execute(
        select(MeetingRoom.id).where(
            MeetingRoom.name == room_name
        )
    )
    db_room_id = db_room_id.scalars().first()
    return db_room_id


async def read_all_rooms_from_db(session: AsyncSession) -> list[MeetingRoom]:
    meeting_room = await session.execute(select(MeetingRoom))
    meeting_room = meeting_room.scalars().all()
    return meeting_room


async def get_meeting_room_by_id(
        room_id: int, session: AsyncSession
) -> Optional[MeetingRoom]:
    search_room = await session.execute(
        select(MeetingRoom).where(MeetingRoom.id == room_id)
    )
    search_room = search_room.scalars().first()
    # search_room = await session.get(MeetingRoom, room_id)  # Можно так...
    return search_room


async def update_meeting_room(
        db_room: MeetingRoom,
        new_data: MeetingRoomUpdate,
        session: AsyncSession
) -> MeetingRoom:
    obj_data = jsonable_encoder(db_room)
    update_data = new_data.model_dump(exclude_unset=True)
    for key in obj_data:
        if key in update_data:
            setattr(db_room, key, update_data[key])
    session.add(db_room)
    await session.commit()
    return db_room
