import os

class Config:
    DB_CONFIG = os.getenv(
        "DB_CONFIG",
        "postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}".format(
            DB_USER=os.getenv("DB_USER", "postgres"),
            DB_PASSWORD=os.getenv("DB_PASSWORD", "postgres1234"),
            DB_HOST=os.getenv("DB_HOST", "localhost"),
            DB_NAME=os.getenv("DB_NAME", "postgres"),
        ),
    )

config = Config
