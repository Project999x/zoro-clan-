#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7692507182:AAECQBOKW8539Kk4q2n0OQw0w2n7RTkXGos")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "19822764"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "b240e413364b8608a542a7cafc6903be")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001985214229"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1418213560"))

#Port
PORT = os.environ.get("PORT", "8051")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://kaido0099878:XR5TnmaT55neAJ2U@cluster0.ksifz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Zoro_Clan_bot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002715726884"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b><blockquote>ʜᴇʏ !! {mention}\n\nɪ ᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ, ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ.</blockquote></b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {mention}\n\n<b>You need to join in my Channel to use me\n\nKindly Please join Channel</b>")

# Start & Fsub Pics ----------------------------------- #
START_PIC = os.environ.get("START_PIC", "https://envs.sh/arr.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://envs.sh/EM8.jpg")
# Start & Fsub Pics ----------------------------------- #

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "<b>❌ Don't send me messages directly I'm only File Share bot !\n👨‍💻 Bot Devloper @WhiteBeard_Sama<\b>"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
