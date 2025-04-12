from pyrogram import Client, filters
from config import OWNER_ID
from queue import get_queue

# Basic in-memory counters (extend with DB if needed)
total_songs = 0
group_ids = set()

@Client.on_message(filters.command("play") & filters.group)
async def track_play(_, message):
    global total_songs
    total_songs += 1
    group_ids.add(message.chat.id)

@Client.on_message(filters.command("stats") & filters.user(OWNER_ID))
async def stats_handler(_, message):
    total_groups = len(group_ids)
    await message.reply(
        f"📊 *Bot Stats:*\n"
        f"• Groups: `{total_groups}`\n"
        f"• Songs Played: `{total_songs}`",
        parse_mode="markdown"
    )

@Client.on_message(filters.command("broadcast") & filters.user(OWNER_ID))
async def broadcast_handler(client, message):
    if len(message.command) < 2:
        return await message.reply("❌ Usage: /broadcast <your message>")

    text = message.text.split(None, 1)[1]
    count = 0

    for gid in group_ids:
        try:
            await client.send_message(gid, text)
            count += 1
        except:
            continue

    await message.reply(f"✅ Broadcast sent to `{count}` groups.", parse_mode="markdown")
