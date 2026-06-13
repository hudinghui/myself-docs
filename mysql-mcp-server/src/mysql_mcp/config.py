from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import tomllib


@dataclass(frozen=True)
class MySQLConfig:
    host: str
    port: int
    user: str
    password: str
    database: str
    connect_timeout: int = 10
    max_limit: int = 1000


DEFAULT_CONFIG_FILE = "config.local.toml"


def load_config(base_dir: str | Path | None = None) -> MySQLConfig:
    config_path = _resolve_config_path(base_dir)
    if config_path is not None:
        return _load_from_file(config_path)

    return MySQLConfig(
        host=_require_env("MYSQL_HOST"),
        port=int(os.getenv("MYSQL_PORT", "3306")),
        user=_require_env("MYSQL_USER"),
        password=_require_env("MYSQL_PASSWORD"),
        database=_require_env("MYSQL_DATABASE"),
        connect_timeout=int(os.getenv("MYSQL_CONNECT_TIMEOUT", "10")),
        max_limit=int(os.getenv("MYSQL_MAX_LIMIT", "1000")),
    )


def _resolve_config_path(base_dir: str | Path | None) -> Path | None:
    configured_path = os.getenv("MYSQL_MCP_CONFIG")
    if configured_path:
        path = Path(configured_path).expanduser()
        if path.is_file():
            return path
        raise RuntimeError(f"MySQL MCP config file does not exist: {path}")

    root = Path(base_dir) if base_dir is not None else Path.cwd()
    candidate = root / DEFAULT_CONFIG_FILE
    if candidate.is_file():
        return candidate
    return None


def _load_from_file(path: Path) -> MySQLConfig:
    data = tomllib.loads(path.read_text())
    return MySQLConfig(
        host=_require_key(data, "host", path),
        port=int(data.get("port", 3306)),
        user=_require_key(data, "user", path),
        password=_require_key(data, "password", path),
        database=_require_key(data, "database", path),
        connect_timeout=int(data.get("connect_timeout", 10)),
        max_limit=int(data.get("max_limit", 1000)),
    )


def _require_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def _require_key(data: dict[str, Any], name: str, path: Path) -> str:
    value = data.get(name)
    if value in (None, ""):
        raise RuntimeError(f"Missing required key `{name}` in {path}")
    return str(value)
