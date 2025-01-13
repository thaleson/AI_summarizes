from dotenv import load_dotenv # type: ignore
import os

def load_env():
    """Carrega as variáveis de ambiente do arquivo .env."""
    load_dotenv()
    return {
        "API_KEY": os.getenv("API_WEB"),
        "MODEL_URL": os.getenv("URL_MODEL")
    }
