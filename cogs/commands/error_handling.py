# Imports
import discord
from discord.ext import commands
from discord.commands import slash_command


class error_handling(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot

    #Slash Command
    @slash_command(description="command3")
    async def hello3(self, ctx: discord.ApplicationContext):
        member = ctx.author
        try:
            await member.edit(nick="Nickname")
        except discord.Forbidden:
            await ctx.respond("I do not have permission to edit the nickname")
            return
        await ctx.respond("The nickname has been edited")


def setup(bot: discord.Bot):
    bot.add_cog(error_handling(bot))
