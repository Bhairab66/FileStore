"""
config.py
---------
Central configuration for the File Store Bot.

IMPORTANT SECURITY NOTE:
Hard-coding secrets (bot tokens, API hashes) directly in source code is not
recommended for production. Prefer environment variables. The values below
fall back to the literals you supplied, but you can (and should) override
them by exporting the corresponding environment variables before running
the bot, e.g.:

    export BOT_TOKEN="xxxx"
    export API_ID="xxxx"
    export API_HASH="xxxx"

Anyone who has seen this bot token in this script (or in any repo/commit
history) can control your bot. If this token has ever been shared publicly,
regenerate it via @BotFather -> /revoke.
"""

import os

# ---------------------------------------------------------------------------
# Core Pyrogram / Telegram credentials
# ---------------------------------------------------------------------------
# API_ID / API_HASH come from https://my.telegram.org -> API Development Tools.
# A bot token alone is NOT enough for Pyrogram; you must supply these too.
API_ID = int(os.environ.get("API_ID", "36237034"))            # <-- fill in your API_ID
API_HASH = os.environ.get("API_HASH", "31c376a5c49eabb8426df4d1f21a5d52")               # <-- fill in your API_HASH
BOT_TOKEN = os.environ.get(
    "BOT_TOKEN",
    "8997630378:AAH3uNrz2bZLqXttAXD2hxOlFoAU398xisM",
)

# ---------------------------------------------------------------------------
# Storage channel (the "database channel"). The bot must be an admin here.
# ---------------------------------------------------------------------------
DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1004341396904"))

# ---------------------------------------------------------------------------
# Local lightweight database (SQLite) - only used to store user IDs, bans,
# generated-link metadata, and settings. Actual files always live in the
# Telegram DB_CHANNEL, never on local disk.
# ---------------------------------------------------------------------------
DB_PATH = os.environ.get("DB_PATH", "filestore.db")

# ---------------------------------------------------------------------------
# Access control
# ---------------------------------------------------------------------------
# Full admins (owners) - comma separated list of user IDs in the env var.
ADMINS = [int(x) for x in os.environ.get("ADMINS", "7053545607").split(",") if x.strip()]

# Moderators - trusted users allowed to run mod-only commands but who are
# not full owners.
MODERATORS = [int(x) for x in os.environ.get("MODERATORS", "7053545607").split(",") if x.strip()]

def is_admin(user_id: int) -> bool:
    return user_id in ADMINS

def is_mod_or_admin(user_id: int) -> bool:
    return user_id in ADMINS or user_id in MODERATORS

# ---------------------------------------------------------------------------
# Force-subscribe channels. Users must join ALL of these before using the
# bot. Use channel IDs (ints, e.g. -1001234567890) or @usernames (strings).
# The bot must be an admin in each of these channels to check membership
# and to generate invite links for private channels.
# ---------------------------------------------------------------------------
FORCE_SUB_CHANNELS = [
    x.strip() for x in os.environ.get("FORCE_SUB_CHANNELS", "-1004318185372").split(",") if x.strip()
]

FORCE_SUB_ALERT_TEXT = (
    "TO USE THIS BOT, YOU MUST JOIN ALL CHANNELS. "
    "JOIN ALL CHANNELS AND PRESS 'TRY AGAIN'."
)

# ---------------------------------------------------------------------------
# Misc
# ---------------------------------------------------------------------------
BOT_USERNAME = os.environ.get("BOT_USERNAME", "My Storage Bot")  # without @, filled in on boot if empty
START_TEXT = (
    "👋 Hello {mention}!\n\n"
    "I'm alive and ready to store & deliver files.\n"
    "Send me a shareable link, or ask an admin to generate one for you."
)
FLOOD_WAIT_SAFETY_SLEEP = 0.00  # seconds between broadcast sends, in addition to FloodWait handling
