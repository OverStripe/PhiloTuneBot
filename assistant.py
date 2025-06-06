import logging
from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN, SESSION_NAME
from plugins.controls import user as voice_user

# Enable logging
logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)

# Initialize Telegram Client (User Account Assistant)
app = Client(
    SESSION_NAME,
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Load Plugins
PLUGINS = [
    "plugins.start",
    "plugins.play",
    "plugins.controls",
    "plugins.leaderboard_cmds",
    "plugins.profile_cmds"
]

for plugin in PLUGINS:
    __import__(plugin)

# Start the Bot
if __name__ == "__main__":
    LOGGER.info("🚀 PhiloTune Assistant Started Successfully!")
    voice_user.start()
    app.run()
