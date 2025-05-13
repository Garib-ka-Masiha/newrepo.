# ---------------------------------------------------
# File Name: users_db.py
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

from config import MONGO_DB
from motor.motor_asyncio import AsyncIOMotorClient as MongoCli
from datetime import datetime, timedelta
import pytz  # Ensure pytz is installed

mongo = MongoCli(MONGO_DB)
db = mongo.users
db = db.users_db


async def get_users():
  user_list = []
  async for user in db.users.find({"user": {"$gt": 0}}):
    user_list.append(user['user'])
  return user_list


async def get_user(user):
  users = await get_users()
  if user in users:
    return True
  else:
    return False

# async def add_user(user):
#   users = await get_users()
#   if user in users:
#     return
#   else:
#     await db.users.insert_one({"user": user})

async def add_user(user):
    users = await get_users()
    if user in users:
        return
    await db.users.insert_one({"user": user, "isBanned": False})

async def ban_user(user):
    user_data =await db.users.find_one({"user": user})
    if user_data:
        # Update the existing user's 'isBanned' status to True
        await db.users.update_one({"user": user}, {"$set": {"isBanned": True}})
    else:
        # Insert user with 'isBanned' set to True if they are not found
        await db.users.insert_one({"user": user, "isBanned": True})


async def is_user_banned(user):
    user_data = await db.users.find_one({"user": user})
    if user_data:
        return user_data.get("isBanned", False)  # Return True if banned, otherwise False
    return False  # Return False if user not found


async def unban_user(user):
    user = int(user)
    user_data =await db.users.find_one({"user": user})
    if user_data:
        # Update the existing user's 'isBanned' status to True
        await db.users.update_one({"user": user}, {"$set": {"isBanned": False}})
    else:
        # Insert user with 'isBanned' set to True if they are not found
        await db.users.insert_one({"user": user, "isBanned": False})


async def del_user(user):
  users = await get_users()
  if not user in users:
    return
  else:
    await db.users.delete_one({"user": user})


async def get_link_count(user_id):
    user = await db.users.find_one({"user": user_id})
    return user.get("link_count", 0) if user else 0


async def update_link_count(user_id):
    user = await db.users.find_one({"user": user_id})
    if not user:
        await add_user(user_id)
        user = await db.users.find_one({"user": user_id})

    tz = pytz.timezone("Asia/Kolkata")  # Change to your timezone if needed
    now = datetime.now(tz)

    last_update = user.get("last_updated_at")
    if last_update:
        last_update = last_update.replace(tzinfo=pytz.utc).astimezone(tz)
    else:
        last_update = now

    # 🔁 Reset time is midnight (00:00)
    reset_time = now.replace(hour=0, minute=0, second=0, microsecond=0)

    if now >= reset_time and last_update < reset_time:
        # If it's a new day and the user's last update was before midnight
        await db.users.update_one(
            {"user": user_id},
            {
                "$set": {
                    "link_count": 1,  # Starts fresh
                    "last_updated_at": datetime.utcnow()
                }
            }
        )
    else:
        # Same day, just increment the counter
        await db.users.update_one(
            {"user": user_id},
            {
                "$inc": {"link_count": 1},
                "$set": {"last_updated_at": datetime.utcnow()}
            }
        )