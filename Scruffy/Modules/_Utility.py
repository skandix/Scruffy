import requests
import socket
import discord
import os
import json
import textwrap

from loguru import logger as log
from discord.ext import commands

from ._Validate import _Validate


class _Utility:
    def __init__(self):
        self._get = requests.get
        self.valid = _Validate()

    def motd(self) -> str:
        """ Gotta need a fancy motd """
        return (
            " _____                  __  __       \n"
            "/  ___|                / _|/ _|      \n"
            "\ `--.  ___ _ __ _   _| |_| |_ _   _ \n"
            " `--. \/ __| '__| | | |  _|  _| | | |\n"
            "/\__/ / (__| |  | |_| | | | | | |_| |\n"
            "\____/ \___|_|   \__,_|_| |_|  \__, |\n"
            "                                __/ |\n"
            "                               |___/ \n"
            "- I'm Scruffy... the Janitor.        \n"
        )

    def _json_pretty(self, data: dict) -> dict:
        return json.dumps(data, indent=4)

    def get_ip(self, domain: str) -> str:
        return socket.gethostbyname(domain)

    def trunk_output(self, output: str):
        return textwrap.shorten(output, width=97, placeholder=" }")

    # TODO: create custom function for embeds
    async def bot_send(self, ctx, data, lang="") -> str:
        if lang == "txt":
            await ctx.send(f"{data}")

        elif lang == "inline":
            await ctx.send(f"``{data}``")

        elif lang == "json":
                await ctx.send(f"```json\n{(self._json_pretty(data))}\n```")

        else:
            log.error(f'Please select one of the langs, {lang} is not supported')
