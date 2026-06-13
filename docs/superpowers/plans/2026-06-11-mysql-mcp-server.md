# MySQL Readonly MCP Server Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a standalone Python MCP server for readonly MySQL access with a schema resource, a guarded query tool, tests, and setup docs.

**Architecture:** Keep SQL validation and query shaping in a pure-Python module that unit tests can cover without external services. Put MCP wiring and MySQL access in a thin server layer that uses FastMCP and a connection helper.

**Tech Stack:** Python 3.11+, FastMCP, mysql-connector-python, unittest

---

### Task 1: Project Skeleton And Tests

**Files:**
- Create: `mysql-mcp-server/pyproject.toml`
- Create: `mysql-mcp-server/README.md`
- Create: `mysql-mcp-server/src/mysql_mcp/__init__.py`
- Create: `mysql-mcp-server/src/mysql_mcp/guards.py`
- Create: `mysql-mcp-server/tests/test_guards.py`

- [ ] **Step 1: Write the failing test**

```python
import unittest

from mysql_mcp.guards import prepare_readonly_query


class PrepareReadonlyQueryTests(unittest.TestCase):
    def test_rejects_update_statements(self):
        with self.assertRaises(ValueError):
            prepare_readonly_query("update users set name = 'x'")
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest mysql-mcp-server/tests/test_guards.py -v`
Expected: FAIL with `ModuleNotFoundError` or missing `prepare_readonly_query`

- [ ] **Step 3: Write minimal implementation**

```python
def prepare_readonly_query(sql: str, limit: int = 200):
    normalized = sql.strip().lower()
    if not normalized.startswith(("select", "with", "explain")):
        raise ValueError("Only SELECT, WITH, and EXPLAIN statements are allowed")
    return sql, limit
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m unittest mysql-mcp-server/tests/test_guards.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add mysql-mcp-server
git commit -m "feat: add mysql mcp server skeleton"
```

### Task 2: SQL Guardrails

**Files:**
- Modify: `mysql-mcp-server/src/mysql_mcp/guards.py`
- Modify: `mysql-mcp-server/tests/test_guards.py`

- [ ] **Step 1: Write the failing test**

```python
    def test_rejects_multiple_statements(self):
        with self.assertRaises(ValueError):
            prepare_readonly_query("select 1; select 2")
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest mysql-mcp-server/tests/test_guards.py -v`
Expected: FAIL because multiple statements are not rejected yet

- [ ] **Step 3: Write minimal implementation**

```python
    stripped = sql.strip().rstrip(";")
    if ";" in stripped:
        raise ValueError("Multiple statements are not allowed")
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m unittest mysql-mcp-server/tests/test_guards.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add mysql-mcp-server/src/mysql_mcp/guards.py mysql-mcp-server/tests/test_guards.py
git commit -m "feat: add readonly sql guardrails"
```

### Task 3: MCP Wiring And Docs

**Files:**
- Create: `mysql-mcp-server/src/mysql_mcp/config.py`
- Create: `mysql-mcp-server/src/mysql_mcp/server.py`
- Modify: `mysql-mcp-server/README.md`

- [ ] **Step 1: Write the failing test**

```python
    def test_coerces_limit_into_supported_range(self):
        sql, limit = prepare_readonly_query("select 1", limit=5000)
        self.assertEqual(limit, 1000)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest mysql-mcp-server/tests/test_guards.py -v`
Expected: FAIL because the limit is not clamped yet

- [ ] **Step 3: Write minimal implementation**

```python
    safe_limit = max(1, min(int(limit), 1000))
    return stripped, safe_limit
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m unittest mysql-mcp-server/tests/test_guards.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add mysql-mcp-server
git commit -m "feat: wire mysql mcp server and docs"
```
