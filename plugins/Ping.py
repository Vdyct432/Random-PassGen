import re
from sys import argv
import platform
import time
from datetime import datetime
from asyncio import sleep
from pyrogram import Client as sree
from pyrogram import filters, __version__ as pyrov
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from main import lol

PING_IMG = "https://telegra.ph/file/67dc081635ccd14064e63.jpg"

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@sree.on_message(filters.command(["ping", "p", "on"]))
async def ping(sree, m: Message):
    start = datetime.now()
    start_time = time.time()
    a = await m.reply("⚡")
    end_time = time.time()
    await sleep(1)
    await a.delete() 
    b = await m.reply_photo(photo=PING_IMG, caption="<i>Pinging... wait!!</i>✨")
    await sleep(1.5)
    uptime = get_readable_time((time.time() - lol))
    py = platform.python_version()
    pong1 = (datetime.now() - start).microseconds / 1000
    pong2 = str(round((end_time - start_time) * 1000, 3)) + " ms"
    ok = await b.edit_text("<b>❍ <u>Ping Pong!</u>🏓</b>\n\n➥ <u><i>Yeah Bot Is Running Perfectly</i></u>!!✨<b>\n\n❅Server Ping: <code>{} ms</code>\n❅Bot Ping</b>: <code>{}</code>\n❅Uptime: <code>{}</code>\n❅Python Version: <code>{}</code>\n❅Pyrogram Version: <code>{}</code>".format(pong1, pong2, uptime, py, pyrov), reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Close", callback_data="close_")]]))
    await m.delete()
    await sleep(120)
    await ok.delete()            
