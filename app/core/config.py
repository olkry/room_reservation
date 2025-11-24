from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_title: str = 'Бронирование переговорок'
    description: str = 'Для персонала'
    database_url: str | None = None
    secret: str = 'SECRET'

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()
