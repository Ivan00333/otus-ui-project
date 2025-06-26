import os
from dotenv import load_dotenv
from utils.logger import logger


load_dotenv()


class AuthConfig:
    try:
        env = os.getenv("ENV", "test").upper()
        login = os.getenv(f"{env}_AUTH_LOGIN")
        password = os.getenv(f"{env}_AUTH_PASSWORD")
    except Exception as e:
        logger.error(f"AuthConfig: не удалось загрузить параметры авторизации: {e}", exc_info=True)
        raise
