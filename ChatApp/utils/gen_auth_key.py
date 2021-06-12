from os import urandom
from ChatApp.database import AuthKey
from pony.orm import db_session


@db_session
def gen_auth_key():
    random = urandom(32)
    while AuthKey.get(auth_key=random):
        random = urandom(32)
    return random
