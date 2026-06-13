import os
import pathlib
import sys
import tempfile
import textwrap
import unittest


PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
sys.path.insert(0, str(SRC_DIR))

from mysql_mcp.config import load_config  # type: ignore  # noqa: E402


class LoadConfigTests(unittest.TestCase):
    def test_prefers_local_toml_file(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = pathlib.Path(tmpdir)
            (root / "config.local.toml").write_text(
                textwrap.dedent(
                    """
                    host = "127.0.0.1"
                    port = 3307
                    user = "readonly_file"
                    password = "secret_file"
                    database = "app_file"
                    connect_timeout = 15
                    max_limit = 500
                    """
                ).strip()
            )

            config = load_config(root)

        self.assertEqual(config.host, "127.0.0.1")
        self.assertEqual(config.port, 3307)
        self.assertEqual(config.user, "readonly_file")
        self.assertEqual(config.password, "secret_file")
        self.assertEqual(config.database, "app_file")
        self.assertEqual(config.connect_timeout, 15)
        self.assertEqual(config.max_limit, 500)

    def test_falls_back_to_environment_variables(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = pathlib.Path(tmpdir)
            previous = {name: os.getenv(name) for name in _CONFIG_ENV_VARS}
            try:
                os.environ["MYSQL_HOST"] = "192.168.1.10"
                os.environ["MYSQL_PORT"] = "3308"
                os.environ["MYSQL_USER"] = "readonly_env"
                os.environ["MYSQL_PASSWORD"] = "secret_env"
                os.environ["MYSQL_DATABASE"] = "app_env"
                os.environ["MYSQL_CONNECT_TIMEOUT"] = "20"
                os.environ["MYSQL_MAX_LIMIT"] = "600"

                config = load_config(root)
            finally:
                for name, value in previous.items():
                    if value is None:
                        os.environ.pop(name, None)
                    else:
                        os.environ[name] = value

        self.assertEqual(config.host, "192.168.1.10")
        self.assertEqual(config.port, 3308)
        self.assertEqual(config.user, "readonly_env")
        self.assertEqual(config.password, "secret_env")
        self.assertEqual(config.database, "app_env")
        self.assertEqual(config.connect_timeout, 20)
        self.assertEqual(config.max_limit, 600)


_CONFIG_ENV_VARS = (
    "MYSQL_HOST",
    "MYSQL_PORT",
    "MYSQL_USER",
    "MYSQL_PASSWORD",
    "MYSQL_DATABASE",
    "MYSQL_CONNECT_TIMEOUT",
    "MYSQL_MAX_LIMIT",
)


if __name__ == "__main__":
    unittest.main()
