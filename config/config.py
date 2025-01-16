import os

API_ID = os.getenv("API_ID") or "YOUR_TELEGRAM_API_ID"
API_HASH = os.getenv("API_HASH") or "YOUR_TELEGRAM_API_HASH"
BOT_TOKEN = os.getenv("BOT_TOKEN") or "YOUR_BOT_TOKEN"
SESSION_NAME = os.getenv("SESSION_NAME") or "YOUR_SESSION_NAME"  # For user account

MONGO_DB_URI = os.getenv("MONGO_DB_URI") or "YOUR_MONGODB_CONNECTION_STRING"
REDIS_URI = os.getenv("REDIS_URI") or "YOUR_REDIS_SERVER_URI"

SUPPORT_CHANNEL = "https://t.me/TechPiroBots"
DEVELOPER_CONTACT = "https://t.me/PiroWise"
