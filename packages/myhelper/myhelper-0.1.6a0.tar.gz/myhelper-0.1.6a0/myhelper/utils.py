"""functions commonly used in other snips"""

__all__ = [
    "generate_random_string",
    "hbs",
    "make_filename_safe",
    "do_it_async"
    ]
__author__ = "Prince Kumar"
__version__ = "0.1.0-alpha"

import re 
import random
import string
import asyncio

def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def hbs(bytes_num):
    """
    Convert bytes to a human-readable format with dynamic precision.
    """
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
    index = 0
    while bytes_num >= 1024 and index < len(suffixes) - 1:
        bytes_num /= 1024.0
        index += 1
    # Format the number with 2 decimal places if it's not an integer,
    # otherwise format it without decimal places
    formatted_num = "{:.2f}".format(bytes_num) if bytes_num % 1 != 0 else "{:.0f}".format(bytes_num)
    return f"{formatted_num} {suffixes[index]}"
    

def make_filename_safe(filename):
    # Replace characters that are not acceptable with an underscore
    safe_filename = re.sub(r'[\\/:*?"<>|]', '_', filename)
    return safe_filename

async def do_it_async(func,*args,**kwargs):
    if not asyncio.get_event_loop().is_running():
      loop = asyncio.new_event_loop()
      asyncio.set_event_loop(loop)
    else:
      loop = asyncio.get_event_loop()
    # Run the synchronous function in a separate thread
    return await loop.run_in_executor(None,func,*args,**kwargs)
