# MySQL Readonly MCP Server

一个最小可运行的 MySQL MCP Server 脚手架，默认只读。

## Features

- MCP `resource`: `schema://tables`
- MCP `tool`: `query_readonly(sql, limit=200)`
- 只允许 `SELECT`、`WITH`、`EXPLAIN`
- 拒绝多语句执行
- 通过 `fetchmany()` 限制返回行数

## Requirements

- Python 3.11+
- MySQL 8+
- 一个只有 `SELECT` 权限的数据库账号

## Install

```bash
cd /Users/edy/devople/doc/mysql-mcp-server
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Local Config File

```bash
cd /Users/edy/devople/doc/mysql-mcp-server
cp config.local.example.toml config.local.toml
```

然后编辑 `config.local.toml`：

```toml
host = "127.0.0.1"
port = 3306
user = "readonly_user"
password = "readonly_password"
database = "app_db"
connect_timeout = 10
max_limit = 1000
```

默认会优先读取项目根目录下的 `config.local.toml`。

## Environment Fallback

如果你不想放本地配置文件，也仍然可以使用环境变量：

```bash
export MYSQL_HOST=127.0.0.1
export MYSQL_PORT=3306
export MYSQL_USER=readonly_user
export MYSQL_PASSWORD=readonly_password
export MYSQL_DATABASE=app_db
export MYSQL_CONNECT_TIMEOUT=10
export MYSQL_MAX_LIMIT=1000
```

如果你想把配置文件放在别的位置，也可以只传一个环境变量：

```bash
export MYSQL_MCP_CONFIG=/absolute/path/to/config.local.toml
```

## Run

```bash
cd /Users/edy/devople/doc/mysql-mcp-server
source .venv/bin/activate
mysql-mcp-server
```

注意：

- 这是 `STDIO` 模式，不要向 `stdout` 打日志
- 如果要记录日志，请写到 `stderr`

## Example MCP Client Config

```json
{
  "mcpServers": {
    "mysql-readonly": {
      "command": "/Users/edy/devople/doc/mysql-mcp-server/.venv/bin/mysql-mcp-server",
      "env": {
        "MYSQL_MCP_CONFIG": "/absolute/path/to/config.local.toml"
      }
    }
  }
}
```

## Codex Config

如果你想直接在 Codex app / CLI / IDE extension 里使用这个 MCP，项目里已经附了一份项目级配置：

`/Users/edy/devople/doc/mysql-mcp-server/.codex/config.toml`

内容如下：

```toml
[mcp_servers.mysql_readonly]
command = "/Users/edy/devople/doc/mysql-mcp-server/.venv/bin/mysql-mcp-server"
cwd = "/Users/edy/devople/doc/mysql-mcp-server"
```

使用方式：

```bash
cd /Users/edy/devople/doc/mysql-mcp-server
source .venv/bin/activate

codex
```

如果你把配置文件放到别处，再把下面这一项补回去即可：

```toml
env_vars = ["MYSQL_MCP_CONFIG"]
```

然后在启动 Codex 前执行：

```bash
export MYSQL_MCP_CONFIG=/absolute/path/to/config.local.toml
```

如果你更想全局生效，也可以把同样的 `[mcp_servers.mysql_readonly]` 配到 `~/.codex/config.toml`。

## Security Notes

- 应用层只做第一道防线，数据库账号本身也必须是只读
- 本项目不会在 `stdout` 输出 SQL
- 返回行数会被限制，但复杂查询本身仍可能很重，建议数据库端再配置超时和资源限制

## Tests

```bash
cd /Users/edy/devople/doc
python3 -m unittest mysql-mcp-server/tests/test_guards.py -v
python3 -m unittest mysql-mcp-server/tests/test_config.py -v
```
