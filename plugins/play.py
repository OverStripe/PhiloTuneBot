from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pytgcalls import PyTgCalls
from pytgcalls.types.stream import StreamAudio
from pytgcalls.types.input_stream import AudioPiped
from config import API_ID, API_HASH, BOT_TOKEN
from utils.downloader import download_song
from utils.generate_card import generate_card
import os

app = Client("MusicBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
call = PyTgCalls(app)

@app.on_message(filters.command("play"))
async def play_music(client, message):
    chat_id = message.chat.id
    if len(message.command) < 2:
        await message.reply("🎵 **Usage:** /play <song_name>")
        return

    query = " ".join(message.command[1:])
    user = message.from_user
    requested_by = f"{user.first_name} {user.last_name or ''}".strip()

    await message.reply(f"🔍 Searching `{query}` on YouTube...")

    # Download song and get metadata
    song_data = download_song(query)
    card = generate_card(song_data['title'], song_data['artist'], song_data['duration'], requested_by, song_data['thumbnail'])

    # Build message
    music_text = f"""
🎧 **Now Playing:** `{song_data['title']}`
🎤 **Artist:** {song_data['artist']}
⏱ **Duration:** {song_data['duration']}
👤 **Requested By:** {requested_by}
📡 **Streaming From:** YouTube
"""

    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("⏸ Pause", callback_data="pause"),
         InlineKeyboardButton("▶ Resume", callback_data="resume")],
        [InlineKeyboardButton("⏹ Stop", callback_data="stop"),
         InlineKeyboardButton("🔄 Skip", callback_data="skip")]
    ])

    await message.reply_photo(photo=open(card, 'rb'), caption=music_text, reply_markup=buttons)

    audio = AudioPiped(song_data['filepath'])
    await call.start()
    await call.join_group_call(chat_id, audio, stream_type=StreamAudio())

@app.on_callback_query()
async def handle_callbacks(client, callback_query):
    chat_id = callback_query.message.chat.id
    data = callback_query.data

    if data == "pause":
        await call.pause_stream(chat_id)
        await callback_query.answer("⏸ Music Paused!")
    elif data == "resume":
        await call.resume_stream(chat_id)
        await callback_query.answer("▶ Music Resumed!")
    elif data == "stop":
        await call.leave_group_call(chat_id)
        await callback_query.answer("⛔ Stopped!")
    elif data == "skip":
        await call.leave_group_call(chat_id)
        await callback_query.answer("⏭ Skipped! (Implement queue logic)")
