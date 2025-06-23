import os
from dotenv import load_dotenv


load_dotenv()


class Environment:
    def __init__(self):
        env = os.getenv("ENV", 'test').upper()
        var_name = f"{env}_URL"
        self.base_url = os.getenv(var_name)
        if not self.base_url:
            raise RuntimeError(f"Переменная {var_name} не задана")

    @property
    def get_base_url(self):
        return self.base_url


host = Environment()
