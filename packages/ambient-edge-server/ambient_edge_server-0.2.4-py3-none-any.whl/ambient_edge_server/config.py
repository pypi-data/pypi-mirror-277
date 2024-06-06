import platform

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ambient_log_level: str = "DEBUG"
    ambient_config: str = "~/.ambientctl/config.json"

    backend_api_url: str = "https://api.ambientlabs.io"
    event_bus_api: str = "https://events.ambientlabs.io"
    connection_service_url: str = "wss://sockets.ambientlabs.io"

    service_template_location: str = (
        "./ambient_edge_server/templates/ambient_edge_server.service.jinja2"
    )
    platform: str = platform.system().lower()


settings = Settings()
