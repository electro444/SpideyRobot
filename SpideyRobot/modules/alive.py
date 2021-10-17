from telethon import events, Button, custom
import re, os
from SpideyRobot.events import register
from SpideyRobot import telethn as tbot
from SpideyRobot import telethn as tgbot
PHOTO = "https://telegra.ph/file/01906842a678a310ca2d1.jpg"
@register(pattern=("/alive"))
async def awake(event):
  PIKACHU = event.sender.first_name
  PIKACHU = "**◐ I Aᴍ Aᴅᴠᴀɴᴄᴇᴅ Scorbunny Rᴏʙᴏᴛ !** \n\n"
  PIKACHU += "**◐ I'ᴍ Wᴏʀᴋɪɴɢ Pʀᴏᴘᴇʀʟʏ**\n\n"
  PIKACHU += "**◐ Sᴘɪᴅᴇʏ! : 2.0 Lᴀᴛᴇsᴛ**\n\n"
  PIKACHU += "**◐ Mʏ Mᴀsᴛᴇʀ :** [Aryanjawale](t.me/Aryanjawale)\n\n"
  PIKACHU += "**◐ Tᴇʟᴇᴛʜᴏɴ Vᴇʀsɪᴏɴ : 1.23.0**\n\n"
  BUTTON = [[Button.url("Sᴜᴘᴘᴏʀᴛ Cʜᴀᴛ", "https://t.me/trainer_zone"), Button.url("Logs Channel", "https://t.me/Scorbunny_logs")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=PIKACHU,  buttons=BUTTON)


__mod_name__ = "Alive"