from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    OPENROUTER_API_KEY: str
    OPENROUTER_MODEL_1: str
    OPENROUTER_MODEL_2: str
    
    model_config = SettingsConfigDict(
    env_file=".env",
    extra="ignore"
)
settings = Settings()