from __future__ import annotations

import json
import sys
from typing import Any

from .config import MySQLConfig, load_config
from .guards import prepare_readonly_query

try:
    import mysql.connector
    from mcp.server.fastmcp import FastMCP
except ImportError as exc:  # pragma: no cover
    missing_dependency_error = exc
    mysql = None
    FastMCP = None
else:
    missing_dependency_error = None


SCHEMA_SQL = """
SELECT
  c.table_name,
  c.column_name,
  c.data_type,
  c.is_nullable,
  c.column_key,
  c.column_default,
  c.column_comment
FROM information_schema.columns AS c
WHERE c.table_schema = %s
ORDER BY c.table_name, c.ordinal_position
""".strip()


def _get_connection(config: MySQLConfig):
    if missing_dependency_error is not None:  # pragma: no cover
        raise RuntimeError(
            "Missing dependencies. Install project dependencies before running the server."
        ) from missing_dependency_error

    return mysql.connector.connect(
        host=config.host,
        port=config.port,
        user=config.user,
        password=config.password,
        database=config.database,
        connection_timeout=config.connect_timeout,
    )


def create_server() -> Any:
    if FastMCP is None:  # pragma: no cover
        raise RuntimeError(
            "FastMCP is unavailable. Run `pip install -e .` inside mysql-mcp-server first."
        ) from missing_dependency_error

    config = load_config()
    mcp = FastMCP("mysql-readonly")

    @mcp.resource("schema://tables")
    def schema_tables() -> str:
        with _get_connection(config) as conn:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(SCHEMA_SQL, (config.database,))
                rows = cursor.fetchall()
        return json.dumps(rows, ensure_ascii=False, indent=2, default=str)

    @mcp.tool()
    def query_readonly(sql: str, limit: int = 200) -> dict[str, Any]:
        safe_sql, safe_limit = prepare_readonly_query(sql, limit=limit, max_limit=config.max_limit)
        with _get_connection(config) as conn:
            with conn.cursor() as cursor:
                cursor.execute(safe_sql)
                columns = [column[0] for column in (cursor.description or [])]
                rows = cursor.fetchmany(size=safe_limit) if columns else []
        return {
            "columns": columns,
            "rows": rows,
            "row_count": len(rows),
            "limit": safe_limit,
        }

    return mcp


def main() -> None:
    try:
        server = create_server()
        server.run()
    except Exception as exc:  # pragma: no cover
        print(f"mysql-mcp-server startup error: {exc}", file=sys.stderr)
        raise


if __name__ == "__main__":
    main()
