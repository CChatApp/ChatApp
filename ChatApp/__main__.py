from ChatApp.config import address, port
from asyncio import get_event_loop, Protocol, gather
from ChatApp.server.errors import bad_request, no_such_method
from ChatApp.server.methods import Mix


def handle(method, rest_of_data):
    try:
        method = int(method, 16)
    except ValueError:
        pass
    else:
        handler = Mix.HANDLERS.get(method)
        if handler:
            handler(rest_of_data)


class TCP(Protocol):
    transport = []

    def connection_made(self, transport) -> None:
        self.transport = transport

    def data_received(self, data: bytes) -> None:
        data = data.decode()
        gather(*[self.handle(packet, self.transport) for packet in data.split(";") if packet])

    @staticmethod
    async def handle(data, transport):
        method, _, packet = data.partition(":")
        try:
            method = int(method, 16)
        except ValueError:
            return transport.write(bad_request.BadRequest("Bad Packet").bytes)
        if method not in Mix.HANDLERS:
            return transport.write(no_such_method.NoSuchMethod("There is no method {}".format(hex(method))).bytes)
        return Mix.HANDLERS[method](packet, transport)


loop = get_event_loop()
coro = loop.create_server(TCP, address, port)
server = loop.run_until_complete(coro)
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
