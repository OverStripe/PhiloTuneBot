from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import SUPPORT_CHANNEL, DEVELOPER_CONTACT
from modules.leaderboard import get_user_rank

# Define roles
DEVELOPER_ID = 7222795580  # Replace with your Telegram ID

@Client.on_message(filters.command("me") & filters.private)
async def user_profile(client, message):
    user = message.from_user
    user_id = user.id
    first_name = user.first_name
    last_name = user.last_name or ""
    username = user.username or "No Username"
    
    # Check if user is the developer
    role = "👑 Developer" if user_id == DEVELOPER_ID else "🎵 Member"

    # Get leaderboard rank
    rank = get_user_rank(user_id)

    # Inline Buttons
    buttons = [
        [InlineKeyboardButton("🏆 View Leaderboard", callback_data="leaderboard")],
        [InlineKeyboardButton("📢 Support", url=SUPPORT_CHANNEL),
         InlineKeyboardButton("👑 Developer", url=DEVELOPER_CONTACT)],
        [InlineKeyboardButton("🔄 Refresh Profile", callback_data="me")]
    ]

    # Send Profile Info
    profile_text = f"""
╭━━━━━━━━━━━━━━━━━╮
   🎭 **USER PROFILE** 🎭
╰━━━━━━━━━━━━━━━━━╯
👤 **Name:** {first_name} {last_name}
🏷 **Username:** @{username}
🔹 **User ID:** {user_id}
🎧 **Songs Played:** {rank['total_plays']}
🏆 **Leaderboard Rank:** #{rank['rank']}

🛠 **Role:** {role}
━━━━━━━━━━━━━━━━━━
💬 **Support Channel:** @TechPiroBots
👑 **Developer:** @PiroWise
━━━━━━━━━━━━━━━━━━
🚀 Keep vibing with the music! 🎶
"""
    
    await message.reply_text(profile_text, reply_markup=InlineKeyboardMarkup(buttons))
