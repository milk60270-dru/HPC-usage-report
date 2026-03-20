"""
SpeedyPizza 資料庫初始化腳本
執行此腳本以建立 SQLite 資料庫並填入範例資料。

使用方式：
    python init_db.py
"""

import sqlite3
import os

DATABASE = "speedypizza.db"
SCHEMA_FILE = "schema.sql"


def init_db():
    """初始化資料庫：建立資料表並填入範例資料"""
    # 如果資料庫已存在，先刪除重建
    if os.path.exists(DATABASE):
        os.remove(DATABASE)
        print(f"已刪除舊的資料庫：{DATABASE}")

    conn = sqlite3.connect(DATABASE)

    with open(SCHEMA_FILE, "r", encoding="utf-8") as f:
        conn.executescript(f.read())

    conn.commit()
    conn.close()
    print(f"資料庫已成功初始化：{DATABASE}")
    print("已建立資料表：pizzas, orders")
    print("已填入範例資料")


if __name__ == "__main__":
    init_db()
