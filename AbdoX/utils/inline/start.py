from pyrogram.types import InlineKeyboardButton

import config
from AbdoX import app

def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضغط لاضافتي لمجموعتك✅", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text="𝐆𝐑𝐎𝐔𝐏", url= "https://t.me/feer3oon"),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضغط لاضافتي لمجموعتك✅",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        
        [
            InlineKeyboardButton(text="مطور السورس ", url=f"https://t.me/W_9_9_9"),
            InlineKeyboardButton(text="𝐆𝐑𝐎𝐔𝐏", url=f"https://t.me/FEER3OON"), 
        ],
        [
            
            InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=f"https://t.me/zzxxue") , 
        ],
    ]
    return buttons
