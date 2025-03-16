from client import tg_client
from telethon import events
from config import CHANNELS_TO_LISTEN


@tg_client.on(events.NewMessage)
async def listen(event: events.NewMessage):
    text = event.text
    if not text:
        return

    print(text)