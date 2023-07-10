from pyrogram import Client, filters
import os
from os import getenv
pyrogram.types import Message

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")

bot = Client('NG_Bot', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


@bot.on_message(filters.command('start'))
def start(client, message):
    message.reply("Hello World")


bot.run()
