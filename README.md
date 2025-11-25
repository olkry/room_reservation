# room_reservation

pip install fastapi==0.115.5 pydantic-settings==2.6.1 "uvicorn[standard]==0.32.1" 

pip install aiosqlite==0.20.0 

pip install "sqlalchemy[asyncio]==2.0.30" 

pip install alembic==1.13.1  
alembic init --template async alembic (инициация алембик в ассинхронном режим в папке алембик)  
alembic revision --autogenerate -m "First migration" (автосоздание миграции с именем после -m)  
alembic upgrade head (выполнит все непремененые миграции)  
alembic downgrade base (полный откат всех применённых миграций)  
alembic history (Просмотр всех миграций в хронологии -v для подробного описания)  
alembic history -i (История с отметкой какая сейчас применена)
alembic current (Посмотреть действующую миграцию)  

alembic revision --autogenerate -m "Initial structure" --rev-id 01  

alembic revision --autogenerate -m "Add new models" --rev-id 02  
При выполнении этих команд файлы будут пронумерованы как задумано:  
01_initial_structure.py  
02_add_new_models.py   


pip install "fastapi-users[sqlalchemy]==13.0.0"

Права доступа для ролей будут такие:  
Анонимный (неаутентифицированный) пользователь
может получить полный список переговорок и интервалы бронирования конкретной переговорки.  
Зарегистрированный пользователь
обладает теми же правами, что и анонимный пользователь, но плюс к тому
может забронировать переговорку;
может получить список своих бронирований;
может обновить или удалить бронь, которую он создал.  
Суперпользователь
обладает теми же правами, что и зарегистрированный, но плюс к тому
может создавать, редактировать и удалять переговорки;
может получать список всех бронирований;
может редактировать и удалять любые объекты бронирования.  


