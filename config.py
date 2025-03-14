import os
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("DB_URL")
BOT_TOKEN = os.getenv("BOT_TOKEN")
CLIENT_API_ID = os.getenv("CLIENT_API_ID")
CLIENT_API_HASH = os.getenv("CLIENT_API_HASH")

CHANNELS_TO_LISTEN = (-1001355713299, )