"""
Configuración central del proyecto.
"""
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

class Settings:
    """
    Clase de configuración central del proyecto.    
    """
    
    GOOGLE_API_KEY: str = os.getenv("GOOGLE_API_KEY", "")

    TAVILY_API_KEY: str = os.getenv("TAVILY_API_KEY", "")

    MODEL_NAME: str = os.getenv(
        "MODEL_NAME",
        "gemini-2.5-flash"
    )

    TEMPERATURE: float = float(
        os.getenv("TEMPERATURE", 0.5)
    )


settings = Settings()
    