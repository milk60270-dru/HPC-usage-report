"""
SpeedyPizza 測試共用的 pytest fixtures
"""

import os
import tempfile
import sqlite3
import pytest
import sys

# 確保專案根目錄在 Python 路徑中
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app import app as flask_app


@pytest.fixture
def app():
    """建立測試用的 Flask 應用程式實例"""
    # 使用暫存檔作為測試資料庫
    db_fd, db_path = tempfile.mkstemp()
    flask_app.config["DATABASE"] = db_path
    flask_app.config["TESTING"] = True

    # 初始化測試資料庫
    with flask_app.app_context():
        conn = sqlite3.connect(db_path)
        schema_path = os.path.join(os.path.dirname(__file__), "..", "schema.sql")
        with open(schema_path, "r", encoding="utf-8") as f:
            conn.executescript(f.read())
        conn.commit()
        conn.close()

    yield flask_app

    # 清理暫存檔
    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    """建立測試用的 HTTP 客戶端"""
    return app.test_client()
