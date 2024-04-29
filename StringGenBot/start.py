from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        msg.chat.id,
        text=f"""★¦ اهلا بـك عزيـزي  {msg.from_user.mention}
★¦ فـي بـوت اسـتـخـراج الـجـلـسـات
★¦ يمكنك استخراج الجلسات الـتالية
★¦ بايروجرام للحسابات & بايروجرام للبوتات
★¦ بـايـروجـرام مـيوزك احـدث إصـدار 
★¦ تيرمـكـس للحسابات & تيرمـكـس للبوتات

★¦ بواسطـة : [𓊆𝘼𝙡𝙈𝙤𝙧𝙝𝙚𝙗𓊇 ⌁ 🚦](tg://user?id=6670911845) √""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="⦓ بـدء اسـتـخـࢪاج جـلـسـة ⦔", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("𝚂𝙾𝚄𝚁𝚂 𝘼𝙡𝙈𝙤𝙧𝙝𝙚𝙗 𓁓", url="https://t.me/HLV_M"),
                    InlineKeyboardButton("ᯓ 𝙳𝙴𝚅 𝘼𝙡𝙈𝙤𝙧𝙝𝙚𝙗 ❥", user_id=6670911845)
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
