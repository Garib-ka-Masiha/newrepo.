# ---------------------------------------------------
# File Name: stats.py
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


import motor
from devgagan import app
from pyrogram import filters
from config import OWNER_ID
from devgagan.core.mongo.users_db import  ban_user , unban_user



@app.on_message(filters.command("ban") & filters.user(OWNER_ID))
async def ban_user_command(client, message):
    user_id = await client.ask(
        OWNER_ID, 
        "Please enter the user ID you want to ban.", 
        filters=filters.text
    )

    user_id = int(user_id.text.strip())  # Extract the actual text input
    print(f"Received user ID: {user_id}")

    await ban_user(user_id)  # Call the actual function to ban the user in the database

    await message.reply(f"Banned user {user_id}")



@app.on_message(filters.command("unban") & filters.user(OWNER_ID))
async def ban_user_command(client, message):
    user_id = await client.ask(
        OWNER_ID, 
        "Please enter the user ID you want to unban.", 
        filters=filters.text
    )

    user_id = int(user_id.text.strip())  # Extract the actual text input
    print(f"Received user ID: {user_id}")

    await unban_user(user_id)  # Call the actual function to ban the user in the database

    await message.reply(f"Unbanned user {user_id}")
