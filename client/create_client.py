from telethon import TelegramClient
from config import CLIENT_API_ID, CLIENT_API_HASH

client = TelegramClient("my_session", CLIENT_API_ID, CLIENT_API_HASH)