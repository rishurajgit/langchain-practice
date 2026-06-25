from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    GOOGLE_API_KEY: str
    MODEL_NAME: str
    
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"  # If extra variables that are not defined, Pydantic will not raise error
    )

settings = Settings()

# print(settings.MODEL_NAME)