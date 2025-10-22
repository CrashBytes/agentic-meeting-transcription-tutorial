"""
Configuration settings for the meeting transcription system.
"""
from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # Application
    APP_NAME: str = "Meeting Transcription System"
    DEBUG: bool = False
    LOG_LEVEL: str = "INFO"
    
    # OpenAI
    OPENAI_API_KEY: str
    OPENAI_MODEL: str = "gpt-4-turbo-preview"
    WHISPER_MODEL: str = "base"  # tiny, base, small, medium, large
    
    # Hugging Face (for Pyannote)
    HUGGINGFACE_TOKEN: str
    
    # Database
    POSTGRES_USER: str = "meeting_user"
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str = "meeting_transcription"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    
    @property
    def DATABASE_URL(self) -> str:
        """Construct async database URL."""
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"
    
    # Qdrant
    QDRANT_URL: str = "http://localhost:6333"
    QDRANT_API_KEY: str | None = None
    QDRANT_COLLECTION_NAME: str = "meeting_transcripts"
    
    # Audio Processing
    MAX_AUDIO_DURATION: int = 7200  # 2 hours in seconds
    CHUNK_SIZE: int = 1024  # bytes
    SAMPLE_RATE: int = 16000  # Hz
    
    # Agent Configuration
    MAX_CONTEXT_TOKENS: int = 8000
    TEMPERATURE: float = 0.7
    MAX_RETRIES: int = 3
    
    # WebSocket
    WS_HEARTBEAT_INTERVAL: int = 30  # seconds
    WS_MAX_SIZE: int = 10 * 1024 * 1024  # 10MB
    
    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()
