import discord

# from ..Modules._Emoji import Emoji

from loguru import logger as log


class pizza_embed:
    def __init__(self):
        self.emojis = {"yes": ":regional_indicator_y:", "no": ":regional_indicator_n:"}

    async def embed_order(self, ctx):
        embed = discord.Embed(
            title="Do you want pizza ?",
            description="Pizza is the best food",
            color=0x3ABCDE,
        )
        embed.add_field(name="Yes", value=self.emojis["yes"], inline=True)
        embed.add_field(name="No", value=self.emojis["no"], inline=True)
        await ctx.send(embed=embed)
        """
        for _, emoji in self.emojis.items():
            log.debug(f"Setting Emoji: {self.get_emoji(emoji)}")
            await msg.add_reaction(emoji)
        """