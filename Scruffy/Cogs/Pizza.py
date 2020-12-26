import discord

from discord.ext import commands
from loguru import logger as log

from ..Modules._Utility import _Utility
from ..Modules._Validate import _Validate
from ..Modules._Emoji import Emoji

from ..Embeds.Pizza import pizza_embed


class Pizza(commands.Cog):
    def __init__(self):
        self._load_cog = True  # if cog should be loaded on startup
        self.valid = _Validate()
        self.misc = _Utility()
        self.pizza = pizza_embed()
        self.emoji = Emoji()

    @commands.command()
    async def order(self, ctx):
        await self.pizza.embed_order(ctx)

    @commands.command()
    async def test(self, ctx, name):
        await self.emoji.get_emoji_id(name)