from modules.config import (
    START_PIC, 
    BOT_USERNAME,
    SUPPORT_GROUP,
    OWNER_USERNAME,
    UPDATES_CHANNEL,
)
from modules.helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message



@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_private(client: Client, message: Message):
 await message.reply_photo(
        photo=f"{START_PIC}",
        caption=f"""**๐ฏุงููุง ุจู  ุงูุง ุจูุช ูุฑูุชูุณ 
โ๏ธุชุดุบูู ุงูุงุบุงูู ูู ุงูููุงููุงุช ุงูุตูุชูุฉ ยป 
โฌ๏ธููุนุฑูุฉ ุงูุงูุงูุฑ ุนููู ุงูููุฑ ุนูู ุฒุฑ ุงูุงูุงูุฑ.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ฏ ยฆ ุงุถููููู ุงูู ููุฌูููุนูุชู ยฆ ๐ฏ",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [
                    InlineKeyboardButton("๐ฅ ยฆ ุงูููููุทูุฑ", url=f"https://t.me/{OWNER_USERNAME}"),
                    InlineKeyboardButton("๐ฅ ยฆ ุงูุฃูุงูููุฑ", url=f"https://telegra.ph/%D9%85%D8%B1%D8%AD%D8%A8%D8%A7-%D8%A8%D9%83%D9%85-%D9%87%D8%B0%D9%87-%D9%87%D9%8A-%D9%82%D8%A7%D8%A6%D9%85%D8%A9-%D8%A7%D9%88%D8%A7%D9%85%D8%B1-%D8%A7%D9%84%D8%A8%D9%88%D8%AA-07-18"),
                ],
                [
                    InlineKeyboardButton(
                        "๐ฅ ยฆ ุงููููุฑูุจ", url=f"{SUPPORT_GROUP}"
                    ),
                    InlineKeyboardButton(
                        "โ๏ธ ยฆ ุงููุณููุฑุณ", url=f"{UPDATES_CHANNEL}"
                    ),
                ],
            ]
        ),
    )


