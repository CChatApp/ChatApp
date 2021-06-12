from asyncio import get_event_loop, Protocol, Transport
from struct import unpack, calcsize, pack, error
from io import BytesIO
from ChatApp.config import address, port
from ChatApp.server.errors import bad_request, no_such_method, ip_is_blocked
from ChatApp.server.methods import Mix
from ChatApp.database.create_db import AuthKey, IP


class TCP(Protocol):
    transport: Transport

    def connection_made(self, transport: Transport) -> None:
        self.transport = transport
        if not IP.get(ip=transport.get_extra_info("peername")[0]):
            IP(ip=transport.get_extra_info("peername")[0])
        else:
            if IP.get(ip=transport.get_extra_info("peername")[0]).blocked:
                return self.send(ip_is_blocked.IPIsBlocked(f"The ip {transport.get_extra_info('peername')[0]} is blocked!").bytes)

    def send(self, data: bytes):
        packed = pack("Q", len(data)) + data
        self.transport.write(packed)

    def data_received(self, data: bytes) -> None:
        try:
            data = BytesIO(data)
            data_len = data.getbuffer().nbytes
            size = unpack("Q", data.read(Q_size))[0]
            buffer = data.read(size)
            self.handle(buffer)
            while data.tell() < data_len:
                size = unpack("Q", data.read(Q_size))[0]
                buffer = data.read(size)
                self.handle(buffer)
        except error:
            self.send(bad_request.BadRequest("Bad Packet").bytes)

    def handle(self, data):
        auth, packet = data[:32], data[33:]
        method, _, data = packet.partition(b":")

        try:
            method_hex = int(method, 16)
        except ValueError:
            return self.send(bad_request.BadRequest("Bad Packet").bytes)

        if auth == temp_auth_key:
            if method_hex not in allowed_methods_temp_auth_key:
                return self.send(bad_request.BadRequest("temp auth key can only be used with GetTemporaryAuthKey").bytes)
            return Mix.HANDLERS[method_hex](data, self)
        else:
            if AuthKey.get(auth_key=auth) is None:
                return self.send(bad_request.BadRequest("wrong auth key").bytes)
            elif method_hex in allowed_methods_temp_auth_key:
                return self.send(bad_request.BadRequest("This method can be accessed only with the default temporary auth key").bytes)
            if method_hex not in Mix.HANDLERS:
                return self.send(no_such_method.NoSuchMethod("There is no method {}".format(hex(method_hex))).bytes)
            return Mix.HANDLERS[method_hex](data, self)


Q_size = calcsize("Q")
loop = get_event_loop()
coro = loop.create_server(TCP, address, port)
server = loop.run_until_complete(coro)
allowed_methods_temp_auth_key = 0xaa197dc2,
temp_auth_key = b'\x9c\xa9\xe2\xb5,c\xc1\xea\xf4\x8f\xf7\x19\xf8\xc5' \
                b'\xd9\xe3G\x88#\xac\x9aW\x1e\x88\t\xdd;4\x80\x97\x08~'


try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
