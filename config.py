import os

API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# List Of Source Channel IDs From Which To Forward
# Example: [-1001234567890, -1009876543210]
SOURCE_CHANNELS = list(map(int, os.environ.get("SOURCE_CHANNELS", "-1003128346880, -1002269913541, -1001971879597").split(",")))

# List Of Target Channel IDs To Forward To
# Example: [-1001234567890, -1009876543210]
TARGET_CHANNELS = list(map(int, os.environ.get("TARGET_CHANNELS", "-1002032204369").split(",")))

WEB_SERVER = os.environ.get("WEB_SERVER", "True").lower() in ("true", "1", "t")
PORT = int(os.environ.get("PORT", "8080"))
PING_INTERVAL = int(os.environ.get("PING_INTERVAL", "300"))

TG_WORKERS = int(os.environ.get("TG_WORKERS", "4"))

# Your Koyeb/Heroku App Url
# Example : https://yorappurl.koyeb.app/
APP_URL = os.environ.get("APP_URL", None)
