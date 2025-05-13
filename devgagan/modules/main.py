# ---------------------------------------------------
# File Name: main.py (Pure Bot, No Userbot)
# Description: Telegram Bot to download/upload with thumbnails
# ---------------------------------------------------

import random
import string
import asyncio
import os
import time
from pyrogram import filters, Client
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from PIL import Image
from datetime import datetime, timedelta

from devgagan import app
from devgagan.core.get_func import get_msg
from devgagan.core.mongo.users_db import is_user_banned, get_link_count, update_link_count
from devgagan.core.mongo.plans_db import get_user_plan
from devgagan.core.func import subscribe, chk_user, get_link
from devgagan.core.mongo import db
from devgagan.modules.shrink import is_user_verified

# Global dictionaries
users_loop = {}
interval_set = {}
batch_mode = {}
user_thumbnails = {}

async def generate_random_name(length=8):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

# Save thumbnail properly
@app.on_message(filters.photo & filters.private)
async def save_thumbnail(client, message):
    user_id = message.chat.id
    download_path = await message.download()

    try:
        img = Image.open(download_path)
        thumb_path = f"{user_id}_thumb.jpg"
        img.convert("RGB").save(thumb_path, "JPEG", quality=75)
        user_thumbnails[user_id] = thumb_path

        await message.reply_text("✅ Thumbnail saved successfully!")
        os.remove(download_path)
    except Exception as e:
        await message.reply_text(f"❌ Failed to save thumbnail: {e}")

# Main function to process and upload files
async def process_and_upload_link(client, user_id, msg_id, link, retry_count, message):
    try:
        original_text = message.text if message.text else ""
        dump_msg = f"{original_text}\nUser ID: {user_id}\nLink: {link}"
        message.text = dump_msg

        thumb = user_thumbnails.get(user_id)
        await get_msg(client, user_id, msg_id, link, retry_count, message, thumb=thumb)
        await asyncio.sleep(15)
    finally:
        pass

async def check_interval(user_id, freecheck):
    if freecheck != 1 or await is_user_verified(user_id):
        return True, None

    now = datetime.now()

    if user_id in interval_set:
        cooldown_end = interval_set[user_id]
        if now < cooldown_end:
            remaining_time = (cooldown_end - now).seconds
            return False, f"Please wait {remaining_time} seconds(s) before sending another link. Alternatively, purchase premium for instant access."
        else:
            del interval_set[user_id]

    return True, None

async def set_interval(user_id, interval_minutes=45):
    now = datetime.now()
    interval_set[user_id] = now + timedelta(seconds=interval_minutes)

async def is_normal_tg_link(link: str) -> bool:
    special_identifiers = ['t.me/+', 't.me/c/', 't.me/b/', 'tg://openmessage']
    return 't.me/' in link and not any(x in link for x in special_identifiers)

# Handler for single link processing
@app.on_message(
    filters.regex(r'https?://(?:www\.)?t\.me/[^\s]+|tg://openmessage\?user_id=\w+&message_id=\d+')
    & filters.private
)
async def single_link(_, message):
    user_id = message.chat.id
    free_check = await chk_user(message, user_id)
    if free_check == 1:
        link_count = await get_link_count(user_id)
        if link_count == FREE_LINK_LIMIT:
            await message.reply(f"You have reached {FREE_LINK_LIMIT} free links per day. Refresh at 12 AM IST.")
            return
        else:
            await update_link_count(user_id)

    buttons = InlineKeyboardMarkup(
        [[InlineKeyboardButton("💬 Contact Owner", url="https://t.me/SungJinHelpBot")]]
    )
    
    user_banned = await is_user_banned(user_id)
    if user_banned:
        return await message.reply(f"Sorry, you are banned by my Owner.", reply_markup=buttons)

    if await subscribe(_, message) == 1 or user_id in batch_mode:
        return

    if users_loop.get(user_id, False):
        await message.reply(f"⚠️ You already have an ongoing process. Please wait or cancel it with /cancel.")
        return

    can_proceed, response_message = await check_interval(user_id, await chk_user(message, user_id))
    if not can_proceed:
        await message.reply(response_message)
        return

    users_loop[user_id] = True
    link = message.text if "tg://openmessage" in message.text else get_link(message.text)
    msg = await message.reply(f"Processing...\nUser ID: {user_id}")

    try:
        if await is_normal_tg_link(link):
            await process_and_upload_link(app, user_id, msg.id, link, 0, message)
            await set_interval(user_id, interval_minutes=45)
        else:
            await msg.edit_text("Invalid or special link. Only normal t.me links are supported.")
    except FloodWait as fw:
        await msg.edit_text(f"⏳ Try again after {fw.x} seconds (FloodWait).")
    except Exception as e:
        await msg.edit_text(f"❌ Error: {e}")
    finally:
        users_loop[user_id] = False
        try:
            await msg.delete()
        except:
            pass

# Cancel handler
@app.on_message(filters.command("cancel") & filters.private)
async def stop_batch(_, message):
    user_id = message.chat.id
    if user_id in users_loop and users_loop[user_id]:
        users_loop[user_id] = False
        await message.reply("✅ Process cancelled successfully!")
    else:
        await message.reply("⚠️ No active process running.")

