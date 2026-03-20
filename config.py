# AWS 設定（透過環境變數取得，避免硬編碼敏感資訊）
import os

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID", "")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", "")
S3_BUCKET_NAME = os.environ.get("S3_BUCKET_NAME", "speedypizza-assets")

# 應用程式設定
SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key-change-in-production")
DATABASE = "speedypizza.db"
DEBUG = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
APP_VERSION = os.environ.get("APP_VERSION", "v1.0.0")
GITHUB_REPO_URL = os.environ.get("GITHUB_REPO_URL", "https://github.com/jeff1121/pizza-lab")
