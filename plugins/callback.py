from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import config
from config import BOT_USERNAME
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery



@Client.on_callback_query(filters.regex("cbcmds"))
async def cbhelps(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Group Music Bot : Help Menu**

__× First Add Me To Your Group..
× Promote Me As Admin In Your Group With All Permission..__

**🏷 Common Commands For Pratheek Music Bot.

•`/play`<song name> - To play song from. YouTube 
•`/audio` - Reply to audio file/YouTube link to play
•`/pause` - To pause currently stream
•`/resume` - To resume currently paused
•`/skip` or `/next` - to change song(work only  if another song is in queue) 
•`/end` or `/stop` - stop/ends music Stream
•`/refresh` or `/restart` - to restart Bot Server(only for heroku) 

            [
                [
                    InlineKeyboardButton(text="🎙️ Support Group 🎙️", url="https://t.me/SHIZUKA_VC_SUPPORT"),
                    InlineKeyboardButton(text="📣 Channel", url=f"https://t.me/aboutpratheek")
                ],
                [
                    InlineKeyboardButton(
                        "🏡 BACK TO HOME", callback_data="cbstart"
                    )
                ]
            ]
        )
    )
