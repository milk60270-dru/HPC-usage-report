# 🍕 SpeedyPizza — 線上披薩訂購系統

![GitHub release (latest by date)](https://img.shields.io/github/v/release/jeff1121/pizza-lab?label=version&logo=github)

SpeedyPizza 是一個使用 Python Flask 和 SQLite 建立的線上披薩訂購系統。
使用者可以瀏覽菜單、下單訂購，並透過訂單編號查詢訂單狀態。

> 本專案為 **DevSecOps 教育訓練** 用途的範例專案。

---

## 功能特色

- 🍕 **披薩菜單**：瀏覽所有可訂購的披薩品項與價格
- 🛒 **線上訂購**：選擇披薩、填寫資料即可下單
- 🔍 **訂單查詢**：透過訂單編號即時查看訂單處理狀態
- 📦 **訂單管理**：追蹤訂單從「準備中」到「已送達」的完整流程

---

## 技術架構

| 項目 | 技術 |
|------|------|
| 後端框架 | Python Flask |
| 資料庫 | SQLite |
| 前端 | HTML + CSS（Jinja2 模板） |
| 測試 | pytest |
| CI/CD | GitHub Actions |

---

## 本地開發環境設定

### 前置需求

- Python 3.9+
- pip

### 安裝步驟

```bash
# 1. 複製專案
git clone <repository-url>
cd pizza-lab

# 2. 建立虛擬環境（建議）
python -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows

# 3. 安裝套件
pip install -r requirements.txt

# 4. 初始化資料庫
python init_db.py

# 5. 啟動應用程式
python app.py
```

啟動後在瀏覽器開啟 http://localhost:5000 即可使用。

### 執行測試

```bash
python -m pytest tests/ -v
```

---

## 專案結構

```
pizza-lab/
├── app.py                  # 主要 Flask 應用程式
├── config.py               # 應用程式設定
├── init_db.py              # 資料庫初始化腳本
├── schema.sql              # 資料表結構定義
├── requirements.txt        # Python 套件清單
├── templates/              # HTML 模板
│   ├── base.html           # 基礎模板
│   ├── index.html          # 首頁（菜單）
│   ├── order.html          # 訂購頁面
│   ├── order_status.html   # 訂單查詢頁面
│   └── order_success.html  # 訂購成功頁面
├── static/
│   └── style.css           # 樣式表
├── tests/                  # 單元測試
│   ├── conftest.py         # 測試 fixtures
│   └── test_app.py         # 應用程式測試
└── .github/
    ├── dependabot.yml      # Dependabot 設定
    └── workflows/
        └── ci.yml          # CI 流程
```

---

## API 端點

| 方法 | 路徑 | 說明 |
|------|------|------|
| GET | `/` | 首頁，顯示披薩菜單 |
| GET | `/order` | 顯示訂購表單 |
| POST | `/order` | 提交訂單 |
| GET | `/order_success` | 訂購成功頁面 |
| GET | `/order_status?order_id=<ID>` | 查詢訂單狀態 |

---

## 授權條款

本專案僅供教育訓練用途。
