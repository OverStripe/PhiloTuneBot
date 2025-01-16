from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from modules.leaderboard import get_top_users

@Client.on_message(filters.command("leaderboard") & filters.private)
async def leaderboard(client, message):
    top_users = get_top_users()
    leaderboard_text = "🏆 **MUSIC LEADERBOARD** 🎶\n━━━━━━━━━━━━━━━━━━\n"

    if not top_users:
        leaderboard_text += "🚀 No songs have been played yet!\n"
    else:
        for i, user in enumerate(top_users, start=1):
            leaderboard_text += f"🥇 {i}. **User ID:** {user['user_id']} - 🎵 {user['plays']} Plays\n"

    buttons = [
        [InlineKeyboardButton("🔄 Refresh Leaderboard", callback_data="leaderboard")],
        [InlineKeyboardButton("📢 Support", url="https://t.me/TechPiroBots")],
        [InlineKeyboardButton("👑 Developer", url="https://t.me/PiroWise")]
    ]

    await message.reply_text(leaderboard_text, reply_markup=InlineKeyboardMarkup(buttons))
