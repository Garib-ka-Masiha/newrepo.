# ---------------------------------------------------
# File Name: start.py
# Description: A Pyrogram bot for downloading files from Telegram channels or groups 
#              and uploading them back to Telegram.
# Author: Gagan
# GitHub: https://github.com/devgaganin/
# Telegram: https://t.me/team_spy_pro
# YouTube: https://youtube.com/@dev_gagan
# Created: 2025-01-11
# Last Modified: 2025-01-11
# Version: 2.0.5
# License: MIT License
# ---------------------------------------------------

from pyrogram import filters
from devgagan import app
from config import OWNER_ID
from devgagan.core.func import subscribe
import asyncio
from devgagan.core.func import *
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.raw.functions.bots import SetBotInfo
from pyrogram.raw.types import InputUserSelf
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from pyrogram.types import BotCommand, InlineKeyboardButton, InlineKeyboardMarkup
 
@app.on_message(filters.command("set"))
async def set(_, message):
    if message.from_user.id not in OWNER_ID:
        await message.reply("You are not authorized to use this command.")
        return
     
    await app.set_bot_commands([
        BotCommand("start", "🚀 Start the bot"),
        BotCommand("batch", "🫠 Extract in bulk"),
        BotCommand("login", "🔑 Get into the bot"),
        BotCommand("logout", "🚪 Get out of the bot"),
        BotCommand("token", "🎲 Get 3 hours free access"),
        BotCommand("adl", "👻 Download audio from 30+ sites"),
        BotCommand("dl", "💀 Download videos from 30+ sites"),
        BotCommand("freez", "🧊 Remove all expired user"),
        BotCommand("pay", "₹ Pay now to get subscription"),
        BotCommand("status", "⟳ Refresh Payment status"),
        BotCommand("transfer", "💘 Gift premium to others"),
        BotCommand("myplan", "⌛ Get your plan details"),
        BotCommand("add", "➕ Add user to premium"),
        BotCommand("rem", "➖ Remove from premium"),
        BotCommand("session", "🧵 Generate Pyrogramv2 session"),
        BotCommand("settings", "⚙️ Personalize things"),
        BotCommand("stats", "📊 Get stats of the bot"),
        BotCommand("plan", "🗓️ Check our premium plans"),
        BotCommand("terms", "🥺 Terms and conditions"),
        BotCommand("speedtest", "🚅 Speed of server"),
        BotCommand("lock", "🔒 Protect channel from extraction"),
        BotCommand("gcast", "⚡ Broadcast message to bot users"),
        BotCommand("help", "❓ If you're a noob, still!"),
        BotCommand("cancel", "🚫 Cancel batch process")
    ])
 
    await message.reply("✅ Commands configured successfully!")
 


# Help message (all in one)
USER_HELP_TEXT = """
**👤 User Commands**

/ꜱᴛᴀʀᴛ – 🚀 ꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ   
/ʙᴀᴛᴄʜ – 🫠 ᴇxᴛʀᴀᴄᴛ ɪɴ ʙᴜʟᴋ   
/ʟᴏɢɪɴ – 🔑 ɢᴇᴛ ɪɴᴛᴏ ᴛʜᴇ ʙᴏᴛ   
/ʟᴏɢᴏᴜᴛ – 🚪 ɢᴇᴛ ᴏᴜᴛ ᴏꜰ ᴛʜᴇ ʙᴏᴛ   
/ᴘᴀʏ – ₹ ᴘᴀʏ ɴᴏᴡ ᴛᴏ ɢᴇᴛ ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ   
/ꜱᴛᴀᴛᴜꜱ – ⟳ ʀᴇꜰʀᴇꜱʜ ᴘᴀʏᴍᴇɴᴛ ꜱᴛᴀᴛᴜꜱ   
/ᴛʀᴀɴꜱꜰᴇʀ – 💘 ɢɪꜰᴛ ᴘʀᴇᴍɪᴜᴍ ᴛᴏ ᴏᴛʜᴇʀꜱ   
/ᴍʏᴘʟᴀɴ – ⌛ ɢᴇᴛ ʏᴏᴜʀ ᴘʟᴀɴ ᴅᴇᴛᴀɪʟꜱ   
/ꜱᴇᴛᴛɪɴɢꜱ – ⚙️ ᴘᴇʀꜱᴏɴᴀʟɪᴢᴇ ᴛʜɪɴɢꜱ   
/ᴘʟᴀɴ – 🗓️ ᴄʜᴇᴄᴋ ᴏᴜʀ ᴘʀᴇᴍɪᴜᴍ ᴘʟᴀɴꜱ   
/ᴛᴇʀᴍꜱ – 🥺 ᴛᴇʀᴍꜱ ᴀɴᴅ ᴄᴏɴᴅɪᴛɪᴏɴꜱ   
/ꜱᴘᴇᴇᴅᴛᴇꜱᴛ – 🚅 ꜱᴘᴇᴇᴅ ᴏꜰ ꜱᴇʀᴠᴇʀ   
/ʜᴇʟᴘ – ❓ ɪꜰ ʏᴏᴜ'ʀᴇ ᴀ ɴᴏᴏʙ, ꜱᴛɪʟʟ!   
/ᴄᴀɴᴄᴇʟ – 🚫 ᴄᴀɴᴄᴇʟ ʙᴀᴛᴄʜ  

"""

ADMIN_HELP_TEXT = """
**🛠️ Owner Commands**

/start – 🚀 Start the bot  
/batch – 🫠 Extract in bulk  
/login – 🔑 Get into the bot  
/logout – 🚪 Get out of the bot  
/freez – 🧊 Remove all expired user  
/pay – ₹ Pay now to get subscription  
/status – ⟳ Refresh Payment status  
/transfer – 💘 Gift premium to others  
/myplan – ⌛ Get your plan details  
/add – ➕ Add user to premium  
/rem – ➖ Remove from premium    
/ban – 🚫 Ban a user from bot  
/unban – ✅ Unban a user  
/session – 🧵 Generate Pyrogramv2 session  
/settings – ⚙️ Personalize things  
/stats – 📊 Get stats of the bot  
/plan – 🗓️ Check our premium plans  
/terms – 🥺 Terms and conditions  
/speedtest – 🚅 Speed of server  
/lock – 🔒 Protect channel from extraction  
/gcast – ⚡ Broadcast message to bot users  
/help – ❓ If you're a noob, still!  
/cancel – 🚫 Cancel batch  
"""



@app.on_message(filters.command("help"))
async def help_command(client, message):
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("👤 User Commands", callback_data="user_help")],
        [InlineKeyboardButton("🛠️ Admin Commands", callback_data="admin_help")]
    ])
    await message.reply("Select an option to see the help commands:", reply_markup=buttons)

@app.on_callback_query(filters.regex("user_help"))
async def user_help_callback(client, callback_query):
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 Back", callback_data="main_help")],
        [InlineKeyboardButton("💎 Subscription Plan", callback_data="subscribe_plans")],
        [InlineKeyboardButton("🆘 Support", url="https://t.me/SungJinHelpBot")]
    ])
    await callback_query.message.edit_text(USER_HELP_TEXT, reply_markup=buttons)

@app.on_callback_query(filters.regex("admin_help"))
async def admin_help_callback(client, callback_query):
    user_id = callback_query.from_user.id
    if user_id in OWNER_ID:
        await callback_query.message.edit_text(ADMIN_HELP_TEXT)
    else:
        await callback_query.answer("🚫You are not authorized to view this.", show_alert=True)

@app.on_callback_query(filters.regex("main_help"))
async def main_help_callback(client, callback_query):
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("👤 User Commands", callback_data="user_help")],
        [InlineKeyboardButton("🛠️ Admin Commands", callback_data="admin_help")]
    ])
    await callback_query.message.edit_text("Select an option to see the help commands:", reply_markup=buttons)

 


 
@app.on_message(filters.command("terms") & filters.private)
async def terms(client, message):
    terms_text = (
        "> 📜 **Terms and Conditions** 📜\n\n"
        "✨ We are not responsible for user deeds, and we do not promote copyrighted content. If any user engages in such activities, it is solely their responsibility.\n"
        "✨ Upon purchase, we do not guarantee the uptime, downtime, or the validity of the plan. __Authorization and banning of users are at our discretion; we reserve the right to ban or authorize users at any time.__\n"
        "✨ Payment to us **__does not guarantee__** authorization for the /batch command. All decisions regarding authorization are made at our discretion and mood.\n"
    )
     
    buttons = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("📋 See Plans", callback_data="subscribe_plans")],
            [InlineKeyboardButton("💬 Contact Now", url="https://t.me/SungJinHelpBot")],
        ]
    )
    await message.reply_text(terms_text, reply_markup=buttons)

@app.on_message(filters.command("plan") & filters.private)
async def plan(client, message):
    plan_msg = "**📌 Click below to check available plans:**"

    buttons = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("💎 View Plans", callback_data="subscribe_plans")],
            [InlineKeyboardButton("⬅️ Back", callback_data="start_menu")]
        ]
    )

    await message.reply_text(plan_msg, reply_markup=buttons)
 


@app.on_callback_query()
async def callback_handler(client, cb: CallbackQuery):
    data = cb.data

    if data == "subscribe_plans":
        await cb.answer("Showing plans...")  # Acknowledge the press
        # Replace with your existing logic for subscribe_plans

    elif data == "delete_msg":
        await cb.answer("Closing...")  # Acknowledge before deleting
        await cb.message.delete()


 


 
 
@app.on_callback_query(filters.regex("see_plan"))
async def see_plan(client, callback_query):
    plan_text = (
        "> 💰**Premium Price**\n\n Starting from $2 or 200 INR accepted via **__ALL PAYMENT APPS__** (terms and conditions apply).\n"
        "📥 **Download Limit**: Users can download up to 100,000 files in a single batch command.\n"
        "🛑 **Batch**: You will get two modes /bulk and /batch.\n"
        "   - Users are advised to wait for the process to automatically cancel before proceeding with any downloads or uploads.\n\n"
        "📜 **Terms and Conditions**: For further details and complete terms and conditions, please send /terms or click See Terms👇\n"
    )
     
    buttons = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("📜 See Terms", callback_data="see_terms")],
            [InlineKeyboardButton("💬 Contact Now", url="https://t.me/NEXUZ_ELITE_BOT")],
        ]
    )
    await callback_query.message.edit_text(plan_text, reply_markup=buttons)
 
 
@app.on_callback_query(filters.regex("see_terms"))
async def see_terms(client, callback_query):
    terms_text = (
        "> 📜 **Terms and Conditions** 📜\n\n"
        "✨ We are not responsible for user deeds, and we do not promote copyrighted content. If any user engages in such activities, it is solely their responsibility.\n"
        "✨ Upon purchase, we do not guarantee the uptime, downtime, or the validity of the plan. __Authorization and banning of users are at our discretion; we reserve the right to ban or authorize users at any time.__\n"
        "✨ Payment to us **__does not guarantee__** authorization for the /batch command. All decisions regarding authorization are made at our discretion and mood.\n"
    )
     
    buttons = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("📋 See Plans", callback_data="subscribe_plans")],
            [InlineKeyboardButton("💬 Contact Now", url="https://t.me/SungJinHelpBot")],
        ]
    )
    await callback_query.message.edit_text(terms_text, reply_markup=buttons)
 
 
