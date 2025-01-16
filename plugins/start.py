from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import SUPPORT_CHANNEL, DEVELOPER_CONTACT

@Client.on_message(filters.command("start") & filters.private)
async def start(client, message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name or ""
    
    # Create Inline Keyboard Buttons
    buttons = [
        [InlineKeyboardButton("🎶 Play Music", callback_data="play")],
        [InlineKeyboardButton("🏆 Leaderboard", callback_data="leaderboard")],
        [
            InlineKeyboardButton("📢 Support", url=SUPPORT_CHANNEL),
            InlineKeyboardButton("👑 Developer", url=DEVELOPER_CONTACT)
        ]
    ]

    # Send Welcome Message
    welcome_text = f"""
╭━━━━━━━━━━━━━━━━━╮
🎵 **Welcome to PhiloTune!** 🎵
╰━━━━━━━━━━━━━━━━━╯
👋 Hello {first_name} {last_name}!
🚀 Enjoy the best music experience with PhiloTune.

💡 Use `/play <song name>` to start playing! 🎶
━━━━━━━━━━━━━━━━━━
💬 **Support Channel:** @TechPiroBots
👑 **Developer:** @PiroWise
━━━━━━━━━━━━━━━━━━
🎵 Let's vibe with music! 🔥🎧
"""
    
    await message.reply_text(welcome_text, reply_markup=InlineKeyboardMarkup(buttons))

