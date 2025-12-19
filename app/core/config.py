from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    api_key: str
    retailcrm_base_url: str

    class Config:
        env_file = ".env"


settings: Settings = Settings()  # type: ignore[call-arg]
