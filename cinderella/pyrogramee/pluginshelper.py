import asyncio
import math
import shlex
import sys
import time
import traceback
from functools import wraps
from typing import Callable, Coroutine, Dict, List, Tuple, Union

from PIL import Image
from pyrogram import Client
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import Chat, Message, User

from cinderella  import OWNER_ID, SUPPORT_CHAT


def get_text(message: Message) -> [None, str]:
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None
