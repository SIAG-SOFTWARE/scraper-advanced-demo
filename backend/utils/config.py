import os
from dotenv import load_dotenv
from typing import Optional

load_dotenv()

class Settings:
    """
    Global configuration loader for the advanced scraper.
    Reads from .env and provides typed access.
    """

    # Target & scraping configs
    TARGET_URL: str = os.getenv("TARGET_URL", "https://example.com/products")
    OUTPUT_MODE: str = os.getenv("OUTPUT_MODE", "csv")  # csv / json / sqlite

    # Proxy configs
    PROXY_SERVER: Optional[str] = os.getenv("PROXY_SERVER")
    PROXY_USERNAME: Optional[str] = os.getenv("PROXY_USERNAME")
    PROXY_PASSWORD: Optional[str] = os.getenv("PROXY_PASSWORD")

    # Captcha solving
    CAPTCHA_API_KEY: Optional[str] = os.getenv("CAPTCHA_API_KEY")

    # Other settings (expandable)
    REQUEST_TIMEOUT: int = 15
    MAX_RETRIES: int = 3

settings = Settings()
