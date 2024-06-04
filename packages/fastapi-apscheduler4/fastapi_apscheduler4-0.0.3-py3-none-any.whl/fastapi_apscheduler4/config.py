"""Configuration models."""

from __future__ import annotations

import os
from enum import Enum
from typing import Annotated, cast

from apscheduler import AsyncScheduler
from pydantic import BaseModel, ConfigDict, Field, PostgresDsn, RedisDsn, SecretStr, computed_field
from pydantic_core import MultiHostUrl, Url
from sqlalchemy.ext.asyncio import AsyncEngine


class SchedulerBroker(str, Enum):
    """Scheduler broker."""

    MEMORY = "memory"
    POSTGRES = "postgres"
    REDIS = "redis"


class SchedulerStore(str, Enum):
    """Scheduler store."""

    MEMORY = "memory"
    POSTGRES = "postgres"


class _BaseConfig(BaseModel):
    """Base Config."""

    model_config = ConfigDict(validate_default=True, arbitrary_types_allowed=True, extra="forbid")


class PostgresConfig(_BaseConfig):
    """Postgres Config."""

    host: str
    port: int = 5432
    user: str | None = None
    password: SecretStr
    db: str

    def get_postgres_dsn(self) -> PostgresDsn:
        """Get Postgres URL."""
        return MultiHostUrl.build(
            scheme="postgresql+asyncpg",
            username=self.user,
            password=self.password.get_secret_value(),
            host=self.host,
            port=self.port,
            path=self.db,
        )

    def get_postgres_url(self) -> str:
        """Get Postgres URL."""
        return self.get_postgres_dsn().unicode_string()


class RedisConfig(_BaseConfig):
    """Redis Config."""

    host: str
    port: int = 6379
    user: str
    password: SecretStr
    db: int = 0
    channel: str = "apscheduler"

    def get_redis_dsn(self) -> RedisDsn:
        """Get the Redis URL."""
        return Url.build(
            scheme="redis",
            username=self.user,
            password=self.password.get_secret_value(),
            host=self.host,
            port=self.port,
            path=str(self.db),
        )

    def get_redis_url(self) -> str:
        """Get the Redis URL."""
        return self.get_redis_dsn().unicode_string()


class APIConfig(_BaseConfig):
    """API Config."""

    prefix: str = "/api/v1"
    tags: list[str | Enum] | None = ["scheduler"]
    include_in_schema: bool = True
    limit_default: Annotated[
        int,
        Field(
            ge=1,
            description=(
                "Page size default limit (only configurable via `SCHEDULER_API_LIMIT_DEFAULT` environment variable)."
            ),
        ),
    ] = cast(int, os.getenv("SCHEDULER_API_LIMIT_DEFAULT", "100"))  # validate default enabled
    limit_max: Annotated[
        int,
        Field(
            ge=1,
            description=(
                "Page size maximum limit (only configurable via `SCHEDULER_API_LIMIT_MAX` environment variable)."
            ),
        ),
    ] = cast(int, os.getenv("SCHEDULER_API_LIMIT_MAX", "1000"))  # validate default enabled


class APSchedulerConfig(_BaseConfig):
    """APScheduler config."""

    broker: SchedulerBroker | None = None
    store: SchedulerStore | None = None
    postgres: PostgresConfig | AsyncEngine | None = None
    redis: RedisConfig | None = None

    @computed_field  # type: ignore[misc] #> mypy issue #1362
    @property
    def computed_broker(self) -> SchedulerBroker:
        """Computed broker."""
        if not self.broker:
            if self.redis:
                return SchedulerBroker.REDIS
            if self.postgres:
                return SchedulerBroker.POSTGRES
            return SchedulerBroker.MEMORY
        return self.broker

    @computed_field  # type: ignore[misc] #> mypy issue #1362
    @property
    def computed_store(self) -> SchedulerStore:
        """Computed store."""
        if not self.store:
            if self.postgres:
                return SchedulerStore.POSTGRES
            return SchedulerStore.MEMORY
        return self.store


class SchedulerConfig(_BaseConfig):
    """FastAPI-APScheduler4 config."""

    auto_start: bool = True
    apscheduler: APSchedulerConfig | AsyncScheduler = APSchedulerConfig()
    api: Annotated[APIConfig | None, Field(description="API configuration (None to disable all API routes).")] = (
        APIConfig()
    )
