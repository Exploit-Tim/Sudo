import os
import platform
import subprocess
import sys
import traceback
from datetime import datetime
from io import BytesIO, StringIO
from PyroUbot.config import OWNER_ID
import psutil
from PyroUbot import *



async def ngentod(client, message):
    remote_url = f"https://{GIT_TOKEN}@github.com/nvaardian/prem.git"
    subprocess.run(["git", "remote", "set-url", "origin", remote_url])

    try:
        out = subprocess.check_output(["git", "pull"], stderr=subprocess.STDOUT).decode("utf-8")

        if "Already up to date." in out:
            return await message.reply(out, quote=True)
        elif len(out) > 4096:
            await send_large_output(message, out)
        else:
            await message.reply(f"```{out}```", quote=True)

        os.execl(sys.executable, sys.executable, "-m", "PyroUbot")

    except subprocess.CalledProcessError as e:
        await message.reply(f"**Gagal pull:**\n```{e.output.decode('utf-8')}```", quote=True)
    except Exception as e:
        await message.reply(f"**Error:** {e}", quote=True)

@PY.BOT("update")
@PY.OWNER
async def _(c, m):
    await ngentod(c, m)


@PY.UBOT("update")
@PY.OWNER
async def _(c, m):
    await ngentod(c, m)
