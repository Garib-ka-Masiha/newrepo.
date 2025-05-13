# ---------------------------------------------------
# File Name: plans_db.py
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

import datetime
from motor.motor_asyncio import AsyncIOMotorClient as MongoCli
from config import OWNER_ID , OWNER_IDS , MONGO_DB
 
mongo = MongoCli(MONGO_DB)
db = mongo.premium
db = db.premium_db
 
# async def add_premium(user_id, expire_date,user_plan):
#     data = await check_premium(user_id)
#     if data and data.get("_id"):
#         await db.update_one({"_id": user_id}, {"$set": {"expire_date": expire_date,"type":user_plan}})
#     else:
#         await db.insert_one({"_id": user_id, "expire_date": expire_date})
#

async def add_premium(user_id, expire_date, user_plan):
    user_plan = user_plan.lower()  # Convert to lowercase
    data = await check_premium(user_id)
    if data and data.get("_id"):
        await db.update_one({"_id": user_id}, {"$set": {"expire_date": expire_date, "type": user_plan}})
    else:
        await db.insert_one({"_id": user_id, "expire_date": expire_date, "type": user_plan})

async def remove_premium(user_id):
    await db.delete_one({"_id": user_id})
 
async def check_premium(user_id):
    return await db.find_one({"_id": user_id})
 
async def premium_users():
    id_list = []
    async for data in db.find():
        id_list.append(data["_id"])
    return id_list


async def get_user_plan(user_id):
    if user_id in OWNER_ID:
        return "diamond"  # Default to 'diamond' if owner id 
    data = await db.find_one({"_id": user_id})
    if data:
            return data.get("type", "free")  # Default to 'free' if no plan is found
    else:
        return "free"

async def check_and_remove_expired_users():
    current_time = datetime.datetime.utcnow()
    async for data in db.find():
        expire_date = data.get("expire_date")
        if expire_date and expire_date < current_time:
            await remove_premium(data["_id"])
            print(f"Removed user {data['_id']} due to expired plan.")
 