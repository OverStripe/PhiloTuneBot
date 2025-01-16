import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped
from yt_dlp import YoutubeDL
from config import SESSION_NAME

# Initialize PyTgCalls for voice chat
app = Client(SESSION_NAME)
call = PyTgCalls(app)

# YouTube Downloader Configuration
ydl_opts = {
    'format': 'bestaudio/best',
    'extractaudio': True,
    'quiet': True,
}

async def get_audio_url(query):
    with YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(f"ytsearch:{query}", download=False)
            url = info['entries'][0]['url']
            title = info['entries'][0]['title']
            return url, title
        except Exception as e:
            return None, None

@Client.on_message(filters.command("play") & filters.group)
async def play_music(client, message: Message):
    chat_id = message.chat.id
    user = message.from_user
    query = " ".join(message.command[1:])

    if not query:
        await message.reply_text("❌ **Please provide a song name or YouTube link!**")
        return

    await message.reply_text("🔍 **Searching... Please wait!**")

    url, title = await get_audio_url(query)
    if not url:
        await message.reply_text("❌ **Song not found. Try another one!**")
        return

    # Play in voice chat
    await call.join_group_call(chat_id, AudioPiped(url), stream_type=StreamType().local_stream)

    # Inline Buttons
    buttons = [
        [
            InlineKeyboardButton("⏸ Pause", callback_data="pause"),
            InlineKeyboardButton("▶️ Resume", callback_data="resume"),
        ],
        [
            InlineKeyboardButton("⏭ Skip", callback_data="skip"),
            InlineKeyboardButton("⏹ Stop", callback_data="stop"),
        ],
    ]

    # Send now playing message
    text = f"""
🎵 **Now Playing:** {title}
🔗 **Source:** YouTube
👤 **Requested By:** {user.first_name} {user.last_name or ""}
🎶 Enjoy your music! 🎧🔥
"""
    await message.reply_text(text, reply_markup=InlineKeyboardMarkup(buttons))
  
