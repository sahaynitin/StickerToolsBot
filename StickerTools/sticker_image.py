import os
from PIL import Image
from pyrogram.types import Message
from pyrogram import Client, filters


@Client.on_message(filters.private & filters.media)
async def media_filter(bot, update):
    try:
        message = await update.reply_text(
            text="Processing...",
            quote=True,
            disable_web_page_preview=True
        )
        media = await update.download()
        await message.edit_text(
            text="Downloading Content to my server...",
            disable_web_page_preview=True
        )
        response = uploadFile(media)
        await message.edit_text(
            text="Uploading...",
            disable_web_page_preview=True
        )
        try:
            os.remove(media)
        except:
            pass
    except Exception as error:
        await update.reply_text(
            text=f"Error :- <code>{error}</code>",
            quote=True,
            disable_web_page_preview=True
        )
        return
    text = f"**File Name:** {response['fileName']}" + "\n"
    text += f"**Download Page:** {response['downloadPage']}" + "\n"
    text += f"**Direct Download Link:** {response['directLink']}" + "\n"
    text += f"**Info:** {response['info']}"
    reply_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="Open Link", url=response['directLink']),
                InlineKeyboardButton(text="Share Link", url=f"https://telegram.me/share/url?url={response['directLink']}")
            ],
            [
                InlineKeyboardButton(text="Join Updates Channel", url="https://telegram.me/FayasNoushad")
            ]
        ]
    )
    await message.edit_text(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )


Bot.run()
