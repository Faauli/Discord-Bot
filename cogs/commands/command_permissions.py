import discord
from discord.ext import commands
from discord.commands import slash_command


class command_permissions(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot

    @slash_command(description="command2")
    @discord.default_permissions(manage_messages=True) # Specifies the permissions required to use the command
    @discord.guild_only() # The command can only be used on servers
    async def hello2(self, ctx: discord.ApplicationContext):
        await ctx.respond(f"This is a slash command")


def setup(bot: discord.Bot):
    bot.add_cog(command_permissions(bot))
