from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from config import SESSION_NAME

app = Client(SESSION_NAME)
call = PyTgCalls(app)

@Client.on_callback_query(filters.regex("pause"))
async def pause_music(client, callback_query):
    await call.pause_stream(callback_query.message.chat.id)
    await callback_query.answer("⏸ Music Paused")

@Client.on_callback_query(filters.regex("resume"))
async def resume_music(client, callback_query):
    await call.resume_stream(callback_query.message.chat.id)
    await callback_query.answer("▶️ Music Resumed")

@Client.on_callback_query(filters.regex("skip"))
async def skip_music(client, callback_query):
    await call.leave_group_call(callback_query.message.chat.id)
    await callback_query.answer("⏭ Song Skipped!")

@Client.on_callback_query(filters.regex("stop"))
async def stop_music(client, callback_query):
    await call.leave_group_call(callback_query.message.chat.id)
    await callback_query.answer("⏹ Music Stopped")
