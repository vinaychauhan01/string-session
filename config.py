from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID","21518327"))
API_HASH = getenv("API_HASH","e72f588b3e4763f01eecfc3c4aa7e8ac")

BOT_TOKEN = getenv("BOT_TOKEN","7152617052:AAHBPQ4cd7-MfuohEt4C8ps-gSedLm41M6U")
MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://vinayjaat:vinay123@vinay1.3yzdb9g.mongodb.net/?retryWrites=true&w=majority")

OWNER_ID = int(getenv("OWNER_ID","5741918628"))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/vs_support_group")
