"""
this v1
v2
SpeedyPizza — 線上披薩訂購系統
一個簡單的 Flask 應用程式，提供披薩菜單瀏覽、線上訂購與訂單查詢功能。
"""

import sqlite3
from flask import Flask, render_template, request, redirect, url_for, g
from config import SECRET_KEY, DATABASE, DEBUG, APP_VERSION, GITHUB_REPO_URL

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY
app.config["DEBUG"] = DEBUG
app.config["APP_VERSION"] = APP_VERSION
app.config["GITHUB_REPO_URL"] = GITHUB_REPO_URL


@app.context_processor
def inject_app_meta():
    """提供全站模板可用的版本與專案資訊"""
    return {
        "app_version": app.config["APP_VERSION"],
        "github_repo_url": app.config["GITHUB_REPO_URL"],
    }


# ============================================================
# 資料庫連線管理
# ============================================================

def get_db():
    """取得當前請求的資料庫連線"""
    if "db" not in g:
        db_path = app.config.get("DATABASE", DATABASE)
        g.db = sqlite3.connect(db_path)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(exception):
    """請求結束時關閉資料庫連線"""
    db = g.pop("db", None)
    if db is not None:
        db.close()


# ============================================================
# 路由定義
# ============================================================

@app.route("/")
def index():
    """首頁：顯示披薩菜單"""
    db = get_db()
    pizzas = db.execute("SELECT * FROM pizzas").fetchall()
    return render_template("index.html", pizzas=pizzas)


@app.route("/order", methods=["GET", "POST"])
def order():
    """下單頁面：選擇披薩並建立訂單"""
    db = get_db()

    if request.method == "POST":
        customer_name = request.form.get("customer_name")
        pizza_id = request.form.get("pizza_id")
        quantity = request.form.get("quantity", 1)

        if customer_name and pizza_id:
            db.execute(
                "INSERT INTO orders (customer_name, pizza_id, quantity) VALUES (?, ?, ?)",
                (customer_name, pizza_id, quantity),
            )
            db.commit()
            return redirect(url_for("order_success"))

    pizzas = db.execute("SELECT * FROM pizzas").fetchall()
    return render_template("order.html", pizzas=pizzas)


@app.route("/order_success")
def order_success():
    """下單成功頁面"""
    return render_template("order_success.html")


@app.route("/order_status")
def order_status():
    """訂單查詢頁面：透過訂單 ID 查詢訂單狀態"""
    order_id = request.args.get("order_id")
    result = None
    error = None

    if order_id:
        db = get_db()
        # ⚠️ 危險：使用字串拼接建構 SQL 查詢
        query = "SELECT orders.id, customer_name, pizzas.name as pizza_name, quantity, status, created_at FROM orders JOIN pizzas ON orders.pizza_id = pizzas.id WHERE orders.id = '" + order_id + "'"
        try:
            result = db.execute(query).fetchone()
            if result is None:
                error = "找不到此訂單編號，請確認後重試。"
        except Exception as e:
            error = f"查詢發生錯誤：{str(e)}"

    return render_template("order_status.html", result=result, error=error, order_id=order_id)


# ============================================================
# 啟動應用程式
# ============================================================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=DEBUG)
