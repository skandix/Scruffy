import discord
import requests
import json

from discord.ext import commands
from loguru import logger as log

from ..Modules._Utility import _Utility
from ..Modules._Validate import _Validate


class NocOrg(commands.Cog):
    def __init__(self):
        self._load_cog = True  # if cog should be loaded on startup
        self._get = lambda url: requests.get(url)
        self.valid = _Validate()
        self.utility = _Utility()

    @commands.command()
    async def ip_rep(self, ctx, ip: str):
        _response = self._get(
            f"https://reputation.noc.org/api/?ip={self.valid.ip(ip)}"
        ).json()

        await self.utility.bot_send(ctx, _response, lang="json")
