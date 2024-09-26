import discord
from discord.ext import commands
from discord.commands import slash_command


class Base(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot

    @slash_command(description="command2")
    @default_permissions(manage_messages=True) # Specifies the permissions required to use the command
    @discord.guild_only() # The command can only be used on servers
    @is_nsfw() # Can only be used by users aged 18 and over, and only in 18+ channels
    async def hello(self, ctx: discord.ApplicationContext):
        await ctx.respond(f"This is a slash command")


def setup(bot: discord.Bot):
    bot.add_cog(Base(bot))
