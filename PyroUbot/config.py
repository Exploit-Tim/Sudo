import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "999"))

DEVS = list(map(int, os.getenv("DEVS", "1927018403").split()))

API_ID = int(os.getenv("API_ID", "27418440"))

API_HASH = os.getenv("API_HASH", "0a08a360e0e9f41b9896f655c300d09d")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8123679703:AAHnB7LpUtfEKvYQdJslVzb5kq61IlKMHII")

OWNER_ID = int(os.getenv("OWNER_ID", "1927018403"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002532595109").split()))

RMBG_API = os.getenv("RMBG_API", "VegrZSZEnnAsufcGsaxECDv6")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://Kinaya:KontolXD#123@kinaya.yuf2elr.mongodb.net/?retryWrites=true&w=majority&appName=Kinaya")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002532595109"))

GIT_TOKEN = os.environ.get("GIT_TOKEN"," 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")
