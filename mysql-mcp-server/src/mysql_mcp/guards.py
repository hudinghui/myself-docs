from __future__ import annotations


ALLOWED_PREFIXES = ("select", "with", "explain")


def prepare_readonly_query(sql: str, limit: int = 200, max_limit: int = 1000) -> tuple[str, int]:
    stripped = sql.strip()
    if not stripped:
        raise ValueError("SQL must not be empty")

    normalized = stripped.rstrip(";").strip()
    if ";" in normalized:
        raise ValueError("Multiple statements are not allowed")

    lowered = normalized.lower()
    if not lowered.startswith(ALLOWED_PREFIXES):
        raise ValueError("Only SELECT, WITH, and EXPLAIN statements are allowed")

    safe_limit = max(1, min(int(limit), int(max_limit)))
    return normalized, safe_limit
