import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Convert API_ID to an integer (fixes invalid literal error)
API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
SESSION_NAME = os.getenv("SESSION_NAME", "")
OWNER_ID = int(os.getenv("OWNER_ID", "0"))
SESSION_STRING = os.getenv("SESSION_STRING", "")

MONGO_DB_URI = os.getenv("MONGO_DB_URI", "")
REDIS_URI = os.getenv("REDIS_URI", "")

SUPPORT_CHANNEL = "https://t.me/TechPiroBots"
DEVELOPER_CONTACT = "https://t.me/PiroWise"
