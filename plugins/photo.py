# By @Darkridersslk
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters


@Client.on_message(filters.photo & filters.private)
async def photo(client: Client, message: Message):
    try:
        await client.send_message(
            chat_id=message.chat.id,
            text="Select your required mode from below!ã¤ã¤",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="đĄ Bright", callback_data="bright"),
                        InlineKeyboardButton(text="đŧ Mixed", callback_data="mix"),
                        InlineKeyboardButton(text="đŗ B&W", callback_data="b|w"),
                    ],
                    [
                        InlineKeyboardButton(text="đĄ Circle", callback_data="circle"),
                        InlineKeyboardButton(text="đŠ¸ Blur", callback_data="blur"),
                        InlineKeyboardButton(text="đ Border", callback_data="border"),
                    ],
                    [
                        InlineKeyboardButton(text="đ Sticker", callback_data="stick"),
                        InlineKeyboardButton(text="âŠī¸ Rotate", callback_data="rotate"),
                        InlineKeyboardButton(text="đĻ Contrast", callback_data="contrast"),
                    ],
                    [
                        InlineKeyboardButton(text="đ Sepia", callback_data="sepia"),
                        InlineKeyboardButton(text="âī¸ Pencil", callback_data="pencil"),
                        InlineKeyboardButton(text="đļ Cartoon", callback_data="cartoon"),
                    ],
                    [
                        InlineKeyboardButton(text="đ Invert", callback_data="inverted"),
                        InlineKeyboardButton(text="đŽ Glitch", callback_data="glitch"),
                        InlineKeyboardButton(
                            text="âī¸ Remove BG", callback_data="removebg"
                        ),
                    ],
                    [
                        InlineKeyboardButton(text="CLOSE", callback_data="close_e"),
                    ],
                ]
            ),
            reply_to_message_id=message.message_id,
        )
    except Exception as e:
        print("photomarkup error - " + str(e))
        if "USER_IS_BLOCKED" in str(e):
            return
        else:
            try:
                await message.reply_text("Something went wrong!", quote=True)
            except Exception:
                return
