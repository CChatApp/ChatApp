from pony.orm import Database, PrimaryKey, Required, Optional, db_session
from os import getcwd, path

database = Database("sqlite", path.join(getcwd(), "clients.db"), create_db=True)


class AuthKey(database.Entity):
    auth_key = PrimaryKey(bytes)
    client = Optional("Client")
    blocked = Required(bool, default=False)


class IP(database.Entity):
    ip = PrimaryKey(str)
    blocked = Required(bool, default=False)


class Client(database.Entity):
    id = PrimaryKey(int, auto=True)
    auth_key = Required(AuthKey)
    ip = Required(str)
    device_model = Required(str)
    official_client = Required(bool, default=False)
    destroyed = Required(bool, default=False)

    # @db_session
    # def insert_or_get(self, ):


database.generate_mapping(create_tables=True)
