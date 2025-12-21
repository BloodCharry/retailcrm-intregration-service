from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    retailcrm_api_key: str
    retailcrm_base_url: str
    retailcrm_site: str
    http_timeout: float = 10.0
    test_offer_id: int | None = None
    # для доступа к FastAPI сервису
    api_key: str

    prometheus_port: int | None = None
    grafana_port: int | None = None
    grafana_admin_user: str | None = None
    grafana_admin_password: str | None = None
    grafana_log_level: str | None = None
    grafana_anonymous_enabled: bool | None = None
    grafana_anonymous_role: str | None = None

    model_config = SettingsConfigDict(env_file=".env")


settings: Settings = Settings()  # type: ignore[call-arg]
