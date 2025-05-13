# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

# bot data 
API_ID = int(getenv("API_ID", "21126899"))
API_HASH = getenv("API_HASH", "b8b981e5913ae632635d36181d7aac57")
BOT_TOKEN = getenv("BOT_TOKEN", "7802266019:AAEx3NtHG9ADpCBqet3TKN97LeSp8qUBnUM")
OWNER_ID = [6167872503]
OWNER_IDS = [6167872503]

#db
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://h12345678:h12345678@cluster0.nxuybhg.mongodb.net/?retryWrites=true&w=majority")
#MONGO_DB = getenv("MONGO_DB", "mongodb+srv://temp:GzWuwc9CsGh8v664@cluster0.cn8sezq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
# logs 

LOG_GROUP = getenv("LOG_GROUP", "-1002503614254")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002503614254"))

#batch limit
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "100"))
SILVER_LIMIT = int(getenv("SILVER_LIMIT", "100"))
GOLD_LIMIT = int(getenv("GOLD_LIMIT", "200"))

#payment data 
DIAMOND_LIMIT = int(getenv("DIAMOND_LIMIT", "1500"))
UPI_ID = str(getenv("UPI","prakharmig51@oksbi"))
UPI_LOGO_FILE = getenv("UPI_LOGO_FILE",None) 

# links limit
FREE_LINK_LIMIT = int(getenv("FREE_LINK_LIMIT",2))
#ads data 
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "")

#string
STRING = getenv("STRING", None)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining

#cookies
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)

#plan prices
SILVER_PRICE = 129
GOLD_PRICE = 179
DIAMOND_PRICE = 249
