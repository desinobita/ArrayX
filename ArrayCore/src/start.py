import asyncio
import os
import sys

from natsort import natsorted
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from time import time
from .. import vcbot, SUDO_USERS, HNDLR, hl 
from Dict.help_dict import HELP_DICT 

HELP = f"""Click The Button Below To Get All Commands 👀."""

Array = "https://telegra.ph/file/fea7a0ef15a02dd5e4aac.jpg"
hehe = "/"
@vcbot.on_message(filters.private & filters.incoming & filters.command(['start'], prefixes=hehe))
async def _start(_, ok: Message):
        Array_msg = f"**Hello [{ok.from_user.first_name}](tg://user?id={ok.from_user.id}) !** \n\n __ • I'm ArrayCore An Advance And Simple Group Voice Call Bot__ \n\n **Click Below Buttons for More Info**"
        await ok.reply_photo(
        photo=Array,
        caption=Array_msg,
        reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton(
                        "• Channel •", url="https://t.me/ArrayCore"),
                    InlineKeyboardButton(
                        "• Support •", url="https://t.me/DNHxHELL")
                ], [
                    InlineKeyboardButton(
                        "• Repo •", url="https://github.com/The-HellBot/ArrayCore")
                ]]
            ))

@vcbot.on_message(filters.command(["help"], prefixes=HNDLR))
async def help_(client: vcbot, e: Message):
    gid = e.chat.id
    bot_us = (await client.get_me()).username
    try:
        id_ = e.from_user.id
    except KeyError:
        await client.send_message(
            gid,
            text="**Click The Button Below To Get All Commands 👀**",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Help", url=f"https://t.me/{bot_us}/?start=help")]])
        )
        return
    buttons = help_btns(id_)
    if gid==id_:
        await client.send_message(gid, text=HELP, reply_markup=buttons)
    else:
        await client.send_message(
            gid,
            text="**Click The Button Below to get Help Menu.**",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Help", url=f"https://t.me/{bot_us}/?start=help")]])
        )

        
@vcbot.on_callback_query(filters.regex(pattern=r"hlplist_(.*)"))
async def help_list_parser(client: vcbot, cq: CallbackQuery):
    await cq.answer()
    user = cq.data.split("_")[1]
    buttons = help_btns(user)
    await cq.edit_message_text(text=HELP, reply_markup=buttons)


@vcbot.on_callback_query(filters.regex(pattern=r"help_(.*)"))
async def help_dicc_parser(client: vcbot, cq: CallbackQuery):
    await cq.answer()
    _, qry, user = cq.data.split("_")
    text = HELP_DICT[qry]
    btn = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data=f"hlplist_{user}")]])
    await cq.edit_message_text(text=text, reply_markup=btn, disable_web_page_preview=True)


def help_btns(user):
    but_rc = []
    buttons = []
    hd_ = list(natsorted(HELP_DICT.keys()))
    for i in hd_:
        but_rc.append(InlineKeyboardButton(i, callback_data=f"help_{i}_{user}"))
        if len(but_rc)==2:
            buttons.append(but_rc)
            but_rc = []
    if len(but_rc)!=0:
        buttons.append(but_rc)
    return InlineKeyboardMarkup(buttons)
