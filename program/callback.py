# Copyright (C) 2021 By AmortMusicProject

from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""โจ **Welcome [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
๐ญ **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) ูุณูุญ ูู ุจุชุดุบูู ุงูููุณููู ูุงูููุฏูู ูู ูุฌููุนุงุช ูู ุฎูุงู ูุญุงุฏุซุงุช ุงูููุฏูู ุงูุฌุฏูุฏุฉ ูู Telegram!**

๐ก **ุงูุชุดู ุฌููุน ุฃูุงูุฑ ุงูุฑูุจูุช ูููููุฉ ุนูููุง ูู ุฎูุงู ุงูููุฑ ููู ยป ๐ Commands button!**

๐ **To know how to use this bot, please click on the ยป โ Basic Guide button!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "โุฃุถููู ุฅูู ูุฌููุนุชูโ",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("โุฏููู ุงูุฃุณุชุฎุฏุงู", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("๐ ุงูุฃูุงูุฑ", callback_data="cbbasic"),
                    InlineKeyboardButton("โค ุงููุงูู", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "๐ฅ ููุงู ุงููููุงุช", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "๐ฃ ููุงู ุงููุทูุฑ", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "๐ ุงูุณูุฑุณ", url="https://t.me/jepthon"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""๐ฆน๐ป ** ุงูุฏููู ุงูุฃุณุงุณู ูุงุณุชุฎุฏุงู ูุฐุง ุงูุฑูุจูุช:**

1.) **ุฃููุง ุ ุฃุถููู ุฅูู ูุฌููุนุชู.**
2.) **ุจุนุฏ ุฐูู ุ ูู ุจุชุฑููุชู ููุณุคูู ูููุญ ุฌููุน ุงูุฃุฐููุงุช ุจุงุณุชุซูุงุก ุงูุชุฎูู.**
3.) **ุจุนุฏ ุชุฑููุชู ุ ุงูุชุจ /reload ูู ูุฌููุนุฉ ูุชุญุฏูุซ ุจูุงูุงุช ุงููุณุคูู.**
3.) **ุฃุถู @{ASSISTANT_NAME} ููุฌููุนุชู ุฃู ุงูุชุจ /userbotjoin ูุฏุนูู ุงูุญุณุงุจ ุงููุณุงุนุฏ.**
4.) ** ูู ุจุชุดุบูู ูุญุงุฏุซุฉ ุงูููุฏูู ุฃููุงู ูุจู ุงูุจุฏุก ูู ุชุดุบูู ุงูููุฏูู / ุงูููุณููู.**
5.) ** ูู ุจุนุถ ุงูุฃุญูุงู ุ ูุชู ุฅุนุงุฏุฉ ุชุญููู ุงูุฑูุจูุช ุจุงุณุชุฎุฏุงู /reload ูููู ุฃู ูุณุงุนุฏู ุงูุฃูุฑ ูู ุญู ุจุนุถ ุงููุดููุงุช.**

๐ **ุฅุฐุง ูู ููุถู ุงููุณุชุฎุฏู bot ุฅูู ุฏุฑุฏุดุฉ ุงูููุฏูู ุ ูุชุฃูุฏ ูู ุชุดุบูู ุฏุฑุฏุดุฉ ุงูููุฏูู ุจุงููุนู ุ ุฃู ุงูุชุจ /userbotleave ุซู ุงูุชุจ/userbotjoin ูุฑู ุงุฎุฑู.**

๐ก **ุฅุฐุง ูุงูุช ูุฏูู ุฃุณุฆูุฉ ูุชุงุจุนุฉ ุญูู ูุฐุง ุงูุฑูุจูุช ุ ูููููู ุฅุฎุจุงุฑู ูู ุฎูุงู ุฏุฑุฏุดุฉ ุงูุฏุนู ุงูุฎุงุตุฉ ุจู ููุง: @{GROUP_SUPPORT}**

โก __Powered by {BOT_NAME} __""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ปโ ุฑุฌูุน", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""๐ฎููุง ุงูุฃูุงูุฑ ุงูุฃุณุงุณูุฉ:

ยป /play (song name/link) -ุชุดุบูู ุงูููุณููู ุนูู ุฏุฑุฏุดุฉ ุงูููุฏูู
ยป /stream (query/link) - ุฏูู ุงูููุณููู ุงูุญูุฉ yt ุงูุญูุฉ / ุงูุฑุงุฏูู
ยป /vplay (video name/link) - ุชุดุบูู ุงูููุฏูู ุนูู ุฏุฑุฏุดุฉ ุงูููุฏูู
ยป /vstream - ุชุดุบูู ููุฏูู ูุจุงุดุฑ ูู yt live / m3u8
ยป /playlist - ุชุธูุฑ ูู ูุงุฆูุฉ ุงูุชุดุบูู
ยป /video (query) - ุชุญููู ุงููุฏูู ูู ุงูููุชููุจ
ยป /song (query) -ุชุญููู ุงุบููุฉ ูู ุงูููุชููุจ
ยป /search (query) -ุงุจุญุซ ุนู ุฑุงุจุท ููุฏูู youtube
ยป /pause - pause the stream
ยป /resume - ุงุณุชุฆูุงู ุงูุชุดุบูู
ยป /skip - ุชุฎุทู ุงูุงุบููู
ยป /stop - ููู ุงูุชุดุบูู
ยป /vmute - ูุชู ุตูุช ุงููุณุชุฎุฏู ุงูุฑูุจูุช ูู ุงูุฏุฑุฏุดุฉ ุงูุตูุชูุฉ
ยป /vunmute - ูู ุจุฅูุบุงุก ูุชู ุตูุช ุงููุณุชุฎุฏู ุงูุฑูุจูุช ูู ุงูุฏุฑุฏุดุฉ ุงูุตูุชูุฉ
ยป /volume `1-200` - ุถุจุท ุญุฌู ุงูููุณููู (ูุฌุจ ุฃู ูููู userbot ูุณุคููุงู)
ยป /reload -ุฃุนุฏ ุชุญููู ุงูุจูุช ููู ุจุชุญุฏูุซ ุจูุงูุงุช ุงููุณุคูู
ยป /userbotjoin - ุฏุนูุฉ ุงููุณุชุฎุฏู ุงูุฑูุจูุช ููุงูุถูุงู ุฅูู ุงููุฌููุนุฉ
ยป /userbotleave -ุทูุจ userbot ูููุบุงุฏุฑุฉ ูู ุงููุฌููุนุฉ
---Sudo---
ยป /rmw - ุชูุธูู ุฌููุน ุงููููุงุช ุงูุฎุงู
ยป /rmd - ุชูุธูู ุฌููุน ุงููููุงุช ุงูุชู ุชู ุชูุฒูููุง
ยป /sysinfo - ุนุฑุถ ูุนูููุงุช ุงููุธุงู
ยป /update - ูู ุจุชุญุฏูุซ ุงูุฑูุจูุช ุงูุฎุงุต ุจู ุฅูู ุฃุญุฏุซ ุฅุตุฏุงุฑ
ยป /restart - ุฃุนุฏ ุชุดุบูู ุงูุฑูุจูุช ุงูุฎุงุต ุจู
ยป /leaveall - ุทูุจ userbot ูููุบุงุฏุฑุฉ ูู ูู ุงููุฌููุนุฉ
---
ยป /ping - ุนุฑุถ ุญุงูุฉ ุงูุจูุช ุจูู
ยป /uptime - ุนุฑุถ ุญุงูุฉ bot ุงูุฌููุฒูุฉ
ยป /alive - ุนุฑุถ ูุนูููุงุช ุงูุฑูุจูุช ุนูู ููุฏ ุงูุญูุงุฉ (ูู ูุฌููุนุฉ)

โก๏ธ __Powered by {BOT_NAME} __""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\nยป revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("๐ก ุงููุณุคูู ุงููุญูุฏ ุงูุฐู ูุฏูู ุฅุฐู ุฅุฏุงุฑุฉ ุงูุฏุฑุฏุดุงุช ุงูุตูุชูุฉ ููููู ุงูููุฑ ุนูู ูุฐุง ุงูุฒุฑ !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"โ๏ธ **settings of** {query.message.chat.title}\n\nโธ : pause stream\nโถ๏ธ : resume stream\n๐ : mute userbot\n๐ : unmute userbot\nโน : stop stream",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("โน", callback_data="cbstop"),
                      InlineKeyboardButton("โธ", callback_data="cbpause"),
                      InlineKeyboardButton("โถ๏ธ", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("๐", callback_data="cbmute"),
                      InlineKeyboardButton("๐", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("๐ Close", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("โ ูุง ุดูุก ูุดุบู ุญุงููุง ", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("๐กุงููุณุคูู ุงููุญูุฏ ุงูุฐู ูุฏูู ุฅุฐู ุฅุฏุงุฑุฉ ุงูุฏุฑุฏุดุงุช ุงูุตูุชูุฉ ููููู ุงูููุฑ ุนูู ูุฐุง ุงูุฒุฑ!", show_alert=True)
    await query.message.delete()
