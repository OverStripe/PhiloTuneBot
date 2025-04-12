from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import AudioPiped
from pytgcalls.types.stream import StreamAudio
from config import SESSION_STRING, API_ID, API_HASH
from queue import skip_current, get_queue, is_active
from utils.generate_card import generate_card
import os

user = Client("VCUser", session_string=SESSION_STRING, api_id=API_ID, api_hash=API_HASH)
call = PyTgCalls(user)

@user.on_callback_query(filters.regex("pause"))
async def pause_music(client, callback_query):
    await call.pause_stream(callback_query.message.chat.id)
    await callback_query.answer("⏸ Music Paused")

@user.on_callback_query(filters.regex("resume"))
async def resume_music(client, callback_query):
    await call.resume_stream(callback_query.message.chat.id)
    await callback_query.answer("▶️ Music Resumed")

@user.on_callback_query(filters.regex("skip"))
async def skip_music(client, callback_query):
    chat_id = callback_query.message.chat.id
    next_song = skip_current(chat_id)
    if next_song:
        audio = AudioPiped(next_song)
        await call.join_group_call(chat_id, audio, stream_type=StreamAudio())
        await callback_query.answer("⏭ Skipped to next song.")
    else:
        await call.leave_group_call(chat_id)
        await callback_query.answer("✅ Queue is empty. Stream ended.")

@user.on_callback_query(filters.regex("stop"))
async def stop_music(client, callback_query):
    chat_id = callback_query.message.chat.id
    await call.leave_group_call(chat_id)
    await callback_query.answer("⏹ Music Stopped")
