from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Settings(BaseSettings):
    retailcrm_api_key: str
    retailcrm_base_url: str
    retailcrm_site: str
    http_timeout: float = 10.0
    test_offer_id: int | None = None

    model_config = ConfigDict(env_file=".env")


settings: Settings = Settings()  # type: ignore[call-arg]
