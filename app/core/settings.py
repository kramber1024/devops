from pydantic_settings import BaseSettings, SettingsConfigDict


class _DatabaseSettings(BaseSettings):
    SCHEME: str = "postgresql+asyncpg://"
    USER: str = "admin"
    PASSWORD: str = "admin"
    HOST: str = "localhost"
    PORT: int = 5432
    DB_NAME: str = "postgres"
    URL: str = f"{SCHEME}{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"


class Settings(BaseSettings):
    database: _DatabaseSettings = _DatabaseSettings()

    model_config = SettingsConfigDict(
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings: Settings = Settings()
