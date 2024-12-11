from telethon import events, Button
from config import MK1, MK2, MK3, MK4, MK5, MK6, MK7, MK8, MK9, MK10
from AltronX.modules.help import *
import telethon

PythonButton = [
        [
        Button.inline("⚡️𝐂ᴏᴍᴍᴀɴᴅs⚡️", data="help_back")
        ],
        [
        Button.url("⚡️𝐂ʜᴀɴɴᴇʟ⚡️", "https://t.me/PROFESSOR_UPDATESX"),
        Button.url("⚡️𝐒ᴜᴘᴘᴏʀᴛ⚡️", "https://t.me/PROFESSOR_UPDATESX")
        ],
        [
        Button.url("⚡️𝗥𝗘𝗣𝗢⚡️", "https://github.com/itzshukla/STRANGER-SPAM-X/fork")
        ]
        ]


@MK1.on(events.NewMessage(pattern="/start"))
@MK2.on(events.NewMessage(pattern="/start"))
@MK3.on(events.NewMessage(pattern="/start"))
@MK4.on(events.NewMessage(pattern="/start"))
@MK5.on(events.NewMessage(pattern="/start"))
@MK6.on(events.NewMessage(pattern="/start"))
@MK7.on(events.NewMessage(pattern="/start"))
@MK7.on(events.NewMessage(pattern="/start"))
@MK8.on(events.NewMessage(pattern="/start"))
@MK9.on(events.NewMessage(pattern="/start"))
@MK10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        AltBot = await event.client.get_me()
        BotName = AltBot.first_name
        BotId = AltBot.id
        TEXT = f"**𝐇ᴇʏ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\n𝗜 𝗔𝗠  [{BotName}](tg://user?id={BotId})​**\n━━━━━━━━━━━━━━━━━━━\n\n"
        TEXT += f"» **✦ 𝐃ᴇᴠᴇʟᴏᴘᴇᴅ 𝐁ʏ :~ [ᴘʀᴏғᴇssᴏʀ](https://t.me/professor_07x)**\n\n"
        TEXT += f"» **𝐏ʀᴏғᴇssᴏʀ 𝐒ᴘᴀᴍ 𝐕ᴇʀsɪᴏɴ:** `3.2`\n"
        TEXT += f"» **𝐓ᴇʟᴇᴛʜᴏɴ 𝐕ᴇʀsɪᴏɴ:** `{telethon.__version__}`\n━━━━━━━━━━━━━━━━━"
        await event.client.send_file(
                event.chat_id,
                "https://files.catbox.moe/59nyop.jpg",
                caption=TEXT, 
                buttons=PythonButton)
