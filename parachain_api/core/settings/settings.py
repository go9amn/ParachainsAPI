from pydantic import BaseSettings

from core.settings.app import AppSettings


class Settings(BaseSettings):
    '''Класс с настройками и переменными всего проекта'''
    app: AppSettings = AppSettings()

    class Config:
        allow_mutation = False
        env_nested_delimiter = '__'
        env_file = '.env'


settings = Settings()
