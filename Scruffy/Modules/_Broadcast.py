# Placeholder class for future thing for sending messages to other channels.


class Broadcast:
    def __init__(self):
        ...

    def send_to_channel(self, ctx):
        channel = client.get_channel(12324234183172)
        await channel.send("hello")
        ...
