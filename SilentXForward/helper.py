import random
import logging
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


START_TEXT = """<b>👋 Hello! I am SilentXForward Bot.</b>

I Can Forward Videos And Documents From Multiple Channels To Multiple Other Channels, Filtering Out Unwanted Content.

<b>Maintained By:</b> <a href="https://t.me/SilentXBotz">SilentXBotz</a>
"""

HELP_TEXT = """<b>ℹ️ Help Menu</b>

I Am An Auto-Forward Bot. I Forward Files From Source Channels To Target Channels.

<b>Commands:</b>
/start - Check If I Am Alive.
/help - Show This Help Message.
/about - Show Information About Me.

<b>How to use:</b>
1. Add Me To Source Channels And Target Channels As Admin.
2. Configure `SOURCE_CHANNELS` and `TARGET_CHANNELS` In Your Environment Variables.
3. I Will Automatically Forward Videos And Documents!

<b>Channel:</b> @SilentXBotz
"""

ABOUT_TEXT = """<b>🤖 About SilentXForward</b>

<b>Name:</b> SilentXForward
<b>Version:</b> 2.0
<b>Channel:</b> <a href="https://t.me/SilentXBotz">SilentXBotz</a>
<b>Repository:</b> <a href="https://github.com/NBBotz/Auto-Forward-Bot">GitHub</a>

<b>Features:</b>
- Multi-Source to Multi-Target
- Video & Document Filter
- FloodWait Handling
"""

BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("📢 Channel", url="https://t.me/SilentXBotz"),
            InlineKeyboardButton("🐱 GitHub", url="https://github.com/NBBotz/Auto-Forward-Bot")
        ]
    ]
)

@Client.on_message(filters.command("start"))
async def start_command(client, message):
    try:
        await message.reply(
            text=START_TEXT,
            parse_mode=enums.ParseMode.HTML,
            reply_markup=BUTTONS,
            disable_web_page_preview=True
        )
    except Exception as e:
        logger.error(f"Error In Start Function: {e}")

@Client.on_message(filters.command("help"))
async def help_command(client, message):
    try:
        await message.reply(
            text=HELP_TEXT,
            parse_mode=enums.ParseMode.HTML,
            reply_markup=BUTTONS,
            disable_web_page_preview=True
        )
    except Exception as e:
        logger.error(f"Error In Help Function: {e}")

@Client.on_message(filters.command("about"))
async def about_command(client, message):
    try:
        await message.reply(
            text=ABOUT_TEXT,
            parse_mode=enums.ParseMode.HTML,
            reply_markup=BUTTONS,
            disable_web_page_preview=True
        )
    except Exception as e:
        logger.error(f"Error In About Function: {e}")
