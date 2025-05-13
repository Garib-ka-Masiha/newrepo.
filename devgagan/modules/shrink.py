from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InputMediaPhoto
import random, string, aiohttp, os, qrcode, asyncio
from PIL import Image
from datetime import datetime, timedelta
from motor.motor_asyncio import AsyncIOMotorClient

from devgagan import app
from devgagan.core.func import *
from devgagan.core.get_func import get_settings_buttons
from config import MONGO_DB, WEBSITE_URL, AD_API, LOG_GROUP, UPI_ID, UPI_LOGO_FILE
from config import OWNER_IDS , SILVER_PRICE , GOLD_PRICE , DIAMOND_PRICE
from telethon import Button

tclient = AsyncIOMotorClient(MONGO_DB)
tdb = tclient["telegram_bot"]
token = tdb["tokens"]
Param = {}

HELP_PAGE_USER = """
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

HELP_PAGE_ADMIN = """
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

PLANS = [
    {
        "name": "Free Plan",
        "icon": "✨",
        "text": """
**✨ Free Plan**  
• 🚫 Ads  
• 🔄 Mode Change  
• 📂 Upload Limit: **2GB/file**  
• 🌐 Save from **Channels & Groups only**  
• 📦 Batch: Not Available  
• ⚙️ Access: Basic Settings Only
""",
        "price": "0"
    },
    {
        "name": "Silver Plan",
        "icon": "⚡",
        "text": """
**⚡ Silver Plan**  
• 🚫 No Ads  
• 🌍 Save from **Everywhere**  
• 🔄 Mode Change  
• 📂 Upload Limit: **4GB/file [Soon]**  
• 📦 Batch Upload: Up to 100 Files  
• ⚙️ Access: Remove, Caption, Logout
""",
        "price": f"{SILVER_PRICE}"
    },
    {
        "name": "Gold Plan",
        "icon": "🔥",
        "text": """
**🔥 Gold Plan/Standard plan**  
• 🚫 No Ads  
• 🌍 Save from **Everywhere**  
• 🔄 Mode Change  
• 📂 Upload Limit: **4GB/file [Soon]**  
• 📦 Batch Upload: Up to 200 Files  
• ♻️ Username Replace/Remove  
• 🖼️ Custom Thumbnail  
• ✏️ Custom Caption  
• 💬 Set Chat ID  
• ⚙️ Access: Full Silver Settings  
• 📞 Support: Available 24*7
""",
        "price": f"{GOLD_PRICE}"
    },
    {
        "name": "Diamond Plan",
        "icon": "🚀",
        "text": """
**🚀 Diamond Plan/Pro plan**  
• 🚫 No Ads  
• 🌍 Save from **Everywhere**  
• 🔄 Mode Change  
• 📂 Upload Limit: **4GB/file [Soon]**  
• 📦 Batch Upload: Up to 1500 Files  
• ♻️ Username Replace/Remove  
• 🖼️ Custom Thumbnail  
• ✏️ Custom Caption  
• ✍️ Text Replace  
• ❌ Text Removal  
• 💬 Set Chat ID  
• ⚙️ Access: All Advanced Features  
• 📞 Support: Available 24*7
""",
        "price": f"{DIAMOND_PRICE}"
    }
]


async def generate_random_param(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


async def get_shortened_url(deep_link):
    api_url = f"https://{WEBSITE_URL}/api?api={AD_API}&url={deep_link}"
    async with aiohttp.ClientSession() as session:
        async with session.get(api_url) as response:
            if response.status == 200:
                data = await response.json()
                if data.get("status") == "success":
                    return data.get("shortenedUrl")
    return None


async def is_user_verified(user_id):
    return await token.find_one({"user_id": user_id}) is not None


def generate_upi_qr(upi_id, amount, logo_path=UPI_LOGO_FILE):
    upi_link = f"upi://pay?pa={upi_id}&pn=Payment&am={amount}&cu=INR"
    qr = qrcode.QRCode(version=5, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
    qr.add_data(upi_link)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

    if logo_path:
        try:
            logo = Image.open(logo_path).convert("RGBA")
            logo_size = qr_img.size[0] // 4
            logo = logo.resize((logo_size, logo_size), Image.LANCZOS)
            qr_with_logo = Image.new("RGBA", qr_img.size)
            qr_with_logo.paste(qr_img, (0, 0))
            pos = ((qr_img.size[0] - logo_size) // 2, (qr_img.size[1] - logo_size) // 2)
            qr_with_logo.paste(logo, pos, logo)
            qr_img = qr_with_logo.convert("RGB")
        except Exception as e:
            print(f"[QR LOGO ERROR] {e}")

    path = f"upi_qr_{amount}.png"
    qr_img.save(path)
    return path


async def render_start_menu(client, chat_id, message=None):
    image_url = "https://envs.sh/dTd.jpg"
    caption = (
        "💾 Welcome to the Ultimate Content Saver Bot on Telegram! 💾\n\n"
        "Steps to Get Started:\n"
        "1. Log in using /login with your number\n"
        "2. Send any Telegram message link\n"
        "3. Tap Settings for premium tools\n\n"
        "🚨 Illegal content will be banned\n"
        "🔔 Follow @SungJinBotz for updates!"
    )

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Subscription", callback_data="subscribe_plans")],
        [InlineKeyboardButton("Settings", callback_data="settings_check"), InlineKeyboardButton("Help", callback_data="help_menu")],
        [InlineKeyboardButton("Support", url="https://t.me/SungJinHelpBot"), InlineKeyboardButton("About", callback_data="about")]
    ])

    if message:
        await message.edit_media(InputMediaPhoto(media=image_url, caption=caption), reply_markup=keyboard)
    else:
        await client.send_photo(chat_id, photo=image_url, caption=caption, reply_markup=keyboard)


@app.on_message(filters.command("start"))
async def start_handler(client, message):
    join = await subscribe(client, message)
    if join == 1:
        return

    user_id = message.chat.id
    param = message.command[1] if len(message.command) > 1 else None
    await render_start_menu(client, message.chat.id)

    if param:
        if await chk_user(message, user_id) != 1:
            await message.reply("You're a premium user, no need for token.")
            return

        if user_id in Param and Param[user_id] == param:
            await token.insert_one({
                "user_id": user_id,
                "param": param,
                "created_at": datetime.utcnow(),
                "expires_at": datetime.utcnow() + timedelta(hours=3),
            })
            del Param[user_id]
            await message.reply("✅ Verified successfully! 3-hour session activated.")
        else:
            await message.reply("❌ Invalid or expired token. Try again.")


@app.on_message(filters.command("help") & filters.private)
async def help_cmd(client, message):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("👤 User Commands", callback_data="help_user")],
        [InlineKeyboardButton("🛠️ Admin Commands", callback_data="help_admin")],
        [InlineKeyboardButton("« Back to Menu", callback_data="start_menu")]
    ])
    await message.reply_text("**❓ Help Menu**\n\nChoose a section to view commands:", reply_markup=keyboard)


async def show_plan_page(cb, page_index):
    """Show a specific plan page with navigation buttons"""
    if page_index < 0 or page_index >= len(PLANS):
        page_index = 0  # Default to first page if out of bounds
    
    plan = PLANS[page_index]
    header = f"**💠 {plan['icon']} {plan['name']} ({page_index + 1}/{len(PLANS)})**\n\n"
    message = header + plan["text"]
    
    keyboard = []
    nav_buttons = []
    
    if page_index > 0:
        nav_buttons.append(InlineKeyboardButton("⬅️ Previous", callback_data=f"plan_page_{page_index - 1}"))
    if page_index < len(PLANS) - 1:
        nav_buttons.append(InlineKeyboardButton("Next ➡️", callback_data=f"plan_page_{page_index + 1}"))
    
    keyboard.append(nav_buttons)
    
    if page_index > 0:  # Not free plan
        keyboard.append([InlineKeyboardButton(f"💰 Buy {plan['name']} - ₹{plan['price']}", 
                        callback_data=f"pay_{plan['name'].lower().split()[0]}_{plan['price']}")])
    
    keyboard.append([InlineKeyboardButton("🔙 Back to Menu", callback_data="start_menu")])
    
    await cb.message.edit_text(message, reply_markup=InlineKeyboardMarkup(keyboard))


# async def open_settings(cb):
#     # Placeholder for settings function - you need to implement the actual settings functionality
#     # Add report errors button to all plans
#     buttons = await get_settings_buttons(user_id)
#     buttons.append([Button.url("Report Errors", "https://t.me/NEXUZ_ELITE_BOT")])
#     message = cb.message
#     await message.edit_text(
#         "⚙️ **Settings Menu**\n\n"
#         "Customize your bot experience here.",
#         buttons=buttons
#     )

async def open_settings(callback_query):
    user_id = callback_query.from_user.id

    # Get your custom buttons (this function needs to return a list of lists of InlineKeyboardButton)
    buttons = await get_settings_buttons(user_id , "pyrogram")

    # Add "Report Errors" button
    buttons.append([InlineKeyboardButton("Report Errors", url="https://t.me/NEXUZ_ELITE_BOT")])

    # Edit the original message
    await callback_query.message.edit_text(
        "⚙️ **Settings Menu**\n\n"
        "Customize your bot experience here.",
        reply_markup=InlineKeyboardMarkup(buttons)
    )

@app.on_callback_query()
async def callback_handler(client, cb: CallbackQuery):
    data = cb.data
    
    if data == "help_user":
        await cb.message.edit_text(
            HELP_PAGE_USER,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("« Back", callback_data="help_menu")]
            ])
        )

    elif data == "help_admin":
        if cb.from_user.id not in OWNER_IDS:
            await cb.answer("You are not allowed to access this.", show_alert=True)
            return
        await cb.message.edit_text(
            HELP_PAGE_ADMIN,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("« Back", callback_data="help_menu")]
            ])
        )

    elif data == "help_menu":
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("👤 User Commands", callback_data="help_user")],
            [InlineKeyboardButton("🛠️ Admin Commands", callback_data="help_admin")],
            [InlineKeyboardButton("« Back to Menu", callback_data="start_menu")]
        ])
        await cb.message.edit_text(
            "**❓ Help Menu**\n\nChoose a section to view commands:",
            reply_markup=keyboard
        )

    elif data == "start_menu":
        await render_start_menu(client, cb.message.chat.id, message=cb.message)

    elif data == "settings_check":
        user_id = cb.from_user.id
        message = cb.message
        
        freecheck = await chk_user(message, user_id)
        
        if freecheck == 1:  # User is free (not premium)
            # Free user: Show upgrade prompt
            text = "**❌ You cannot use this feature.**\n\nPlease upgrade to Premium to access advanced settings."
            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton("💎 Subscription Plans", callback_data="subscribe_plans")],
                [InlineKeyboardButton("⬅️ Back", callback_data="start_menu")]
            ])
            await message.edit_text(text, reply_markup=keyboard)
        else:
            # Premium or higher plan user: show loading then trigger settings
            await cb.message.edit_text("⚙️ Loading your settings...", reply_markup=None)
            await asyncio.sleep(1)  # optional short delay to simulate loading
            await open_settings(cb)
    
    elif data == "about":
        await cb.message.edit_text(
            "⍟───[ MY ᴅᴇᴛᴀɪʟꜱ ]───⍟\n\n"
            "‣ ᴍʏ ɴᴀᴍᴇ : Sung jin  2\n"
            "‣ ᴅᴇᴠᴇʟᴏᴘᴇʀ : Mr. Sung \n"
            "‣ ʟɪʙʀᴀʀʏ : Pyrogram\n"
            "‣ ʟᴀɴɢᴜᴀɢᴇ : Python 3\n"
            "‣ ᴅᴀᴛᴀʙᴀꜱᴇ : MongoDB\n"
            "‣ ʙᴏᴛ ꜱᴇʀᴠᴇʀ : Heroku\n"
            "‣ ʙᴜɪʟᴅ : v2.7.1 [Stable]",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("« Back", callback_data="start_menu")]])
        )
    
    elif data == "subscribe_plans":
        await show_plan_page(cb, 0)
    
    elif data.startswith("plan_page_"):
        page_index = int(data.split("_")[-1])
        await show_plan_page(cb, page_index)
    
    elif data.startswith("pay_"):
        parts = data.split("_")
        plan_key, plan_price = parts[1], parts[2]
        
        # Get plan name based on plan key
        plan_name = "Unknown Plan"
        for plan in PLANS:
            if plan["name"].lower().split()[0] == plan_key.lower():
                plan_name = plan["name"]
                break

        upi_id = UPI_ID
        qr_path = generate_upi_qr(upi_id, plan_price)  # Generate the QR code dynamically

        payment_text = (
            f"🛒 **Make Payment for: {plan_name}**\n"
            f"💰 **Amount:** ₹{plan_price}\n\n"
            "📸 **Send a screenshot of the payment for verification.**"
        )

        premium = InlineKeyboardButton("📤 Send Screenshot Here", url="https://t.me/NEXUZ_ELITE_BOT")
        keyboard = InlineKeyboardMarkup([
            [premium]
        ])

        await client.send_photo(chat_id=cb.message.chat.id, photo=qr_path, caption=payment_text,
                                reply_markup=keyboard)
        os.remove(qr_path)
