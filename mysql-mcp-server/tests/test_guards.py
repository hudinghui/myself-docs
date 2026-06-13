import pathlib
import sys
import unittest


PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
sys.path.insert(0, str(SRC_DIR))

from mysql_mcp.guards import prepare_readonly_query  # type: ignore  # noqa: E402


class PrepareReadonlyQueryTests(unittest.TestCase):
    def test_allows_select_statements(self):
        sql, limit = prepare_readonly_query("select * from users", limit=20)
        self.assertEqual(sql, "select * from users")
        self.assertEqual(limit, 20)

    def test_rejects_write_statements(self):
        with self.assertRaisesRegex(
            ValueError, "Only SELECT, WITH, and EXPLAIN statements are allowed"
        ):
            prepare_readonly_query("update users set name = 'x'")

    def test_rejects_multiple_statements(self):
        with self.assertRaisesRegex(ValueError, "Multiple statements are not allowed"):
            prepare_readonly_query("select 1; select 2")

    def test_clamps_limit_to_maximum(self):
        _, limit = prepare_readonly_query("select * from users", limit=5000)
        self.assertEqual(limit, 1000)

    def test_clamps_limit_to_minimum(self):
        _, limit = prepare_readonly_query("select * from users", limit=0)
        self.assertEqual(limit, 1)


if __name__ == "__main__":
    unittest.main()
