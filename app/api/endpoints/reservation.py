from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.schemas.reservation import ReservationDB, ReservationCreate
from app.api.endpoints.validators import (
    check_meeting_room_exists, check_reservation_intersections
)
from app.crud.reservation import reservation_crud

router = APIRouter()

SessionDep = Annotated[AsyncSession, Depends(get_async_session)]

@router.post(
    '/',
    response_model=ReservationDB,
)
async def create_reservation(
    reservation: ReservationCreate,
    session: SessionDep,
):
    await check_meeting_room_exists(
        reservation.meetingroom_id, session
    )
    await check_reservation_intersections(
        **reservation.model_dump(), session=session
    )
    new_reservation = await reservation_crud.create(
        reservation, session
    )
    return new_reservation
