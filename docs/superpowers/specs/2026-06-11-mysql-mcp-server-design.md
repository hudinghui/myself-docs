# MySQL Readonly MCP Server Design

## Goal

Create a standalone MCP server for MySQL that exposes schema metadata as an MCP resource and readonly SQL execution as an MCP tool.

## Scope

- Transport: STDIO for local MCP hosts
- Database: MySQL
- Access mode: readonly only
- Resource: `schema://tables`
- Tool: `query_readonly(sql, limit=200)`

## Non-Goals

- Write operations
- Auth proxying beyond standard MySQL credentials
- HTTP transport
- Query history, caching, or pagination

## Architecture

The project will be a small Python package. Pure validation and SQL-shaping logic will live in a separate module so it can be unit-tested without requiring MCP or MySQL client libraries. The MCP entrypoint will wire those helpers to FastMCP and a MySQL connection layer.

## Behavior

### Resource: `schema://tables`

Returns table, column, nullability, key information, defaults, and comments from `information_schema` for the selected database.

### Tool: `query_readonly`

- Accepts raw SQL text and an optional row limit
- Allows only statements beginning with `SELECT`, `WITH`, or `EXPLAIN`
- Rejects multiple statements
- Applies a bounded row limit before execution
- Returns column names, rows, and row count

## Security

- Application-level SQL guardrails reject non-readonly statements
- The README will require a MySQL account with `SELECT` privileges only
- The server will not log query contents to stdout

## Testing

- Unit tests cover SQL normalization, readonly checks, multi-statement rejection, and limit coercion
- The project will not require a live MySQL server for core tests
