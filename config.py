import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    TG_BOT_TOKEN = "5863446083:AAELdsq0fAbKdCKaMDIGQmfE98vJ0JvDSmQ"
    APP_ID = 5587539
    API_HASH = "8670b598fef377e6782429b1f664dce6"
    TG_USER_SESSION = ""
    DB_URI = ""

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
