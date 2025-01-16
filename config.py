import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Convert API_ID to an integer to avoid ValueError
API_ID = int(os.getenv("API_ID", "0"))  # Default to 0 if not set
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
SESSION_NAME = os.getenv("SESSION_NAME", "")

MONGO_DB_URI = os.getenv("MONGO_DB_URI", "")
REDIS_URI = os.getenv("REDIS_URI", "")

SUPPORT_CHANNEL = "https://t.me/TechPiroBots"
DEVELOPER_CONTACT = "https://t.me/PiroWise"
