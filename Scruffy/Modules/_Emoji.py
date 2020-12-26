import discord


class Emoji:
    def __init__(self):
        self.guild = discord.utils.get(bot.guilds, name="")

    def get_emoji_id(self, emoji_name: str) -> str:
        return discord.utils.get(self.guild.emojis, name=emoji_name)

    def add_emoji(self, emoji_nr: int) -> str:
        return bot.get_emoji(emoji_nr)
