import discord
from discord.ext import commands
from discord.commands import slash_command


class slash_command(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot

    @slash_command(description="command1")
    async def hello(self, ctx: discord.ApplicationContext):
        await ctx.respond(f"This is a slash command")


def setup(bot: discord.Bot):
    bot.add_cog(slash_command(bot))
