
from sqlite_utils import hookimpl
import sqlite_utils_sqlite_lembed

__version__ = "0.0.1a4"
__version_info__ = tuple(__version__.split("."))

@hookimpl
def prepare_connection(conn):
  conn.enable_load_extension(True)
  sqlite_utils_sqlite_lembed.load(conn)
  conn.enable_load_extension(False)
