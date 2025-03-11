import os
from dotenv import load_dotenv

load_dotenv()
DB_URL = os.getenv("DB_URL")
BOT_TOKEN = os.getenv("BOT_TOKEN")