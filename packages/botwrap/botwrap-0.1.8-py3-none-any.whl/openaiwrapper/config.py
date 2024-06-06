# Path: C:\Users\jamig\OneDrive\Desktop\botwrap\openaiwrapper\config.py

import os

class Config:
    """Base configuration class."""
    LOG_FILE = os.getenv("LOG_FILE", "application.log")
    API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
    API_KEY = os.getenv("OPENAI_API_KEY")

    @classmethod
    def validate(cls):
        if not cls.API_KEY:
            raise ValueError("API_KEY is not set.")
        if not cls.API_BASE_URL:
            raise ValueError("API_BASE_URL is not set.")
        if not cls.LOG_FILE:
            raise ValueError("LOG_FILE is not set.")

class DevelopmentConfig(Config):
    """Development environment configuration."""
    TEAM_MEMBERS = [
        {"id": "1", "name": "ParserAssistant", "role": "parser", "instructions": "Parse tasks", "model": "gpt-4-turbo"},
        {"id": "2", "name": "ExecutorAssistant", "role": "executor", "instructions": "Execute tasks", "model": "gpt-4-turbo"},
    ]

class ProductionConfig(Config):
    """Production environment configuration."""
    TEAM_MEMBERS = [
        {"id": "1", "name": "ParserAssistant", "role": "parser", "instructions": "Parse tasks", "model": "gpt-4-turbo"},
        {"id": "2", "name": "ExecutorAssistant", "role": "executor", "instructions": "Execute tasks", "model": "gpt-4-turbo"},
    ]

def get_config(environment: str = 'development') -> Config:
    config_mapping = {
        'development': DevelopmentConfig,
        'production': ProductionConfig,
        'staging': Config  # Assuming 'staging' should use base configurations
    }
    if environment not in config_mapping:
        raise ValueError(f"Invalid environment: {environment}")
    config_class = config_mapping[environment]
    config_class.validate()
    return config_class

def get_environment() -> str:
    return os.getenv("ENVIRONMENT", "development")
