import asyncio
import logging
import threading
import time
import urllib.request
from aiohttp import web
from pyrogram import Client
from SilentXForward.forward import process_queue
from SilentXForward import web_server
from config import API_ID, API_HASH, BOT_TOKEN, TG_WORKERS, WEB_SERVER, PORT, APP_URL

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def ping_loop():
    while True:
        try:
            with urllib.request.urlopen(APP_URL, timeout=10) as response:
                if response.status == 200:
                    logger.info("✅ Ping Successful")
                else:
                    logger.error(f"⚠️ Ping Failed: {response.status}")
        except Exception as e:
            logger.debug(f"❌ Exception During Ping: {e}")
        time.sleep(300)

if APP_URL:
    threading.Thread(target=ping_loop, daemon=True).start()
    
async def create_server():
    try:
        app = web.AppRunner(await web_server())
        await app.setup()
        await web.TCPSite(app, "0.0.0.0", PORT).start()
        logger.info(f"Web server started on port {PORT}")
    except Exception as e:
        logger.error(f"Failed to start web server: {e}")

class Bot(Client):
    def __init__(self):
        super().__init__(
            "SilentXForwardBot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=TG_WORKERS,
            sleep_threshold=10,
            plugins={"root": "SilentXForward"}
        )

    async def start(self, *args, **kwargs):
        await super().start(*args, **kwargs)
        me = await self.get_me()
        logger.info(f"Bot Started! Name: {me.first_name} (@{me.username})")
        if WEB_SERVER:
            await create_server()
        asyncio.create_task(process_queue(self))
        

    async def stop(self, *args, **kwargs):
        await super().stop(*args, **kwargs)
        logger.info("Bot Stopped")


if __name__ == '__main__':
    Bot().run()
