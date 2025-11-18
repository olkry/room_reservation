from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

# from app.crud.meeting_room import (
#     create_meeting_room, get_room_id_by_name, read_all_rooms_from_db,
#     get_meeting_room_by_id, update_meeting_room, delete_meeting_room
# )  До CRUD ред.
from app.crud.meeting_room import meeting_room_crud
from app.schemas.meeting_room import (
    MeetingRoomCreate, MeetingRoomDB, MeetingRoomUpdate
)
from app.core.db import get_async_session
from .validators import check_meeting_room_exists, check_name_duplicate

# router = APIRouter(
#     prefix='/meeting_rooms',
#     tags=['Meeting Rooms']
# ) Это всё переносим в routers.py

router = APIRouter()

SessionDep = Annotated[AsyncSession, Depends(get_async_session)]


@router.post(
    '/',
    response_model=MeetingRoomDB,
    response_model_exclude_none=True,
)
async def create_new_meeting_room(
    meeting_room: MeetingRoomCreate,
    session: SessionDep,
):
    await check_name_duplicate(meeting_room.name, session)
    # new_room = await create_meeting_room(meeting_room, session) До CRUD ред.
    new_room = await meeting_room_crud.create(meeting_room, session)
    return new_room


@router.get(
    '/',
    response_model=list[MeetingRoomDB],
    response_model_exclude_none=True,
)
async def get_all_meeting_rooms(session: SessionDep):
    # rooms = await read_all_rooms_from_db(session=session) До CRUD ред.
    all_rooms = await meeting_room_crud.get_multi(session)
    return all_rooms


@router.patch(
    '/{meeting_room_id}',
    response_model=MeetingRoomDB,
    response_model_exclude_none=True,
)
async def partially_update_meeting_room(
    meeting_room_id: int,
    obj_in: MeetingRoomUpdate,
    session: SessionDep,
):
    meeting_room = await check_meeting_room_exists(meeting_room_id, session)
    if obj_in.name is not None:
        await check_name_duplicate(obj_in.name, session)

    # meeting_room = await update_meeting_room(meeting_room, obj_in, session) До CRUD ред.
    meeting_room = await meeting_room_crud.update(
        meeting_room, obj_in, session
    )
    return meeting_room


@router.delete(
    '/{meeting_room_id}',
    response_model=MeetingRoomDB,
    response_model_exclude_none=True,
)
async def remove_meeting_room(
    meeting_room_id: int,
    session: SessionDep,
):
    meeting_room = await check_meeting_room_exists(meeting_room_id, session)
    # meeting_room = await delete_meeting_room(meeting_room, session) До CRUD ред.
    meeting_room = await meeting_room_crud.remove(meeting_room, session)
    return meeting_room
