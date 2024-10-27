import discord
from discord.ext import commands
from discord.commands import slash_command

class embeds(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot
      
    @slash_command(description="Embed")
    async def send_embed(self, ctx):
        embed = discord.Embed(
            title="Title",
            description="Description",
            color=0x00FF00 # Color
        )
        embed.add_field(name="Field-Title", value="This is a field")

        await ctx.respond(embed=embed)

def setup(bot: discord.Bot):
    bot.add_cog(embeds(bot))
