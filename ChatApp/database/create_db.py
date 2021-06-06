from pony.orm import Database, PrimaryKey, Required
from os import getcwd, path

database = Database("sqlite", path.join(getcwd(), "clients.db"), create_db=True)


class Client(database.Entity):
    id = PrimaryKey(int, auto=True)
    auth_key = Required(str)
    ip = Required(str)
    device_model = Required(str)
    official_client = Required(bool, default=False)
    destroyed = Required(bool, default=False)
