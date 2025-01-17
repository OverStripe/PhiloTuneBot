from pytgcalls import PyTgCalls
from pytgcalls.types.stream import StreamType  # ✅ Fixed Import Path
from pytgcalls.types.input_stream import AudioPiped
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Initialize PyTgCalls client
app = Client("MusicBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
call = PyTgCalls(app)

@app.on_message(filters.command("play"))
async def play_music(client, message):
    chat_id = message.chat.id
    if len(message.command) < 2:
        await message.reply("🎵 **Usage:** /play <song_name>")
        return
    
    song_name = message.command[1]
    user = message.from_user
    requested_by = f"{user.first_name} {user.last_name or ''}"

    # 🎵 New Stylish Now Playing Format
    music_text = f"""
🎧 **Now Playing:** `{song_name}`
🎶 **Source:** YouTube
🎤 **Requested By:** {requested_by}
📡 **Streaming...**
"""

    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("⏸ Pause", callback_data="pause"),
         InlineKeyboardButton("▶ Resume", callback_data="resume")],
        [InlineKeyboardButton("⏹ Stop", callback_data="stop"),
         InlineKeyboardButton("🔄 Skip", callback_data="skip")]
    ])

    await message.reply(music_text, reply_markup=buttons)

    # Dummy example to play audio (Replace with actual streaming logic)
    audio = AudioPiped("https://sample-videos.com/audio/mp3/wave.mp3")
    await call.start()
    await call.join_group_call(chat_id, audio, stream_type=StreamType().local_stream)

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
        await callback_query.message.edit_text("🛑 **Music Stopped!**")
    elif data == "skip":
        await callback_query.message.edit_text("🔄 **Skipping Track...**")

app.run()
