from fastapi import APIRouter

# Импортируем модули, в которых описаны роутеры:
from app.api.endpoints import (
    meeting_room_router, reservation_router, user_router
)

# Создаём главный роутер:
main_router = APIRouter()
# Подключаем роутеры из модулей к главному роутеру:
main_router.include_router(
    meeting_room_router, prefix='/meeting_rooms', tags=['Meeting Rooms']
)
main_router.include_router(
    reservation_router, prefix='/reservations', tags=['Reservations']
)
main_router.include_router(user_router)
