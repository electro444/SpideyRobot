from telethon import events, Button, custom
import re, os
from SpideyRobot.events import register
from SpideyRobot import telethn as tbot
from SpideyRobot import telethn as tgbot
PHOTO = "https://telegra.ph/file/f65cb56e8a7f3f184962b.jpg"
@register(pattern=("/alive"))
async def awake(event):
  PIKACHU = event.sender.first_name
  PIKACHU = "**◐ I Aᴍ Aᴅᴠᴀɴᴄᴇᴅ Scorbunny !** \n\n"
  PIKACHU += "**◐ I'ᴍ Wᴏʀᴋɪɴɢ Pʀᴏᴘᴇʀʟʏ**\n\n"
  PIKACHU += "**◐ Scorbunny! : 2.0 Lᴀᴛᴇsᴛ**\n\n"
  PIKACHU += "[**◐ Mʏ Mᴀsᴛᴇʀ :**](t.me/Aryanjawale)\n\n"
  PIKACHU += "**◐ Tᴇʟᴇᴛʜᴏɴ Vᴇʀsɪᴏɴ : 1.23.0**\n\n"
  BUTTON = [[Button.url("Sᴜᴘᴘᴏʀᴛ Cʜᴀᴛ", "https://t.me/trainer_zone"),
  BUTTON = [[Button.url("Pigasus Support", "https://t.me/PigasusSupport")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=PIKACHU,  buttons=BUTTON)


__mod_name__="Alive"
