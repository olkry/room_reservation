from app.core.db import AsyncSessionLocal
from app.models.meeting_room import MeetingRoom
from app.schemas.meeting_room import MeetingRoomCreate


async def create_meeting_room(new_room: MeetingRoomCreate) -> MeetingRoom:
    # Конвертируем объект MeetingRoomCreate в словарь.
    new_room_data = new_room.model_dump()
    db_room = MeetingRoom(**new_room_data)

    # Создаём асинхронную сессию через контекстный менеджер.
    async with AsyncSessionLocal() as session:
        # Добавляем созданный объект в сессию.
        # Никакие действия с базой пока ещё не выполняются.
        session.add(db_room)

        # Записываем изменения непосредственно в БД.
        # Так как сессия асинхронная, используем ключевое слово await.
        await session.commit()

    # Возвращаем только что созданный объект класса MeetingRoom.
    return db_room
