import discord
import ezcord
from discord.ext import tasks
from discord.commands import slash_command

class autodelete(ezcord.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.autodelete1.start()

    @tasks.loop(seconds=180)
    async def autodelete1(self):
        channel_id = # Your Channel ID
        channel = self.bot.get_channel(channel_id)
        messages = await channel.history(limit=200).flatten()
        for message in messages:
            if not message.pinned:
                await message.delete()

    @autodelete1.before_loop
    async def before_autodelete(self):
        await self.bot.wait_until_ready()

    @slash_command(description="Sends the auto-delete message."")
    async def autodelete(self, ctx):
        channel_id = # Your Channel ID
        channel = self.bot.get_channel(channel_id)
        embed = discord.Embed(
            title="",
            description="# 🚨 | Autodelete \n The auto-delete is active in this channel; messages are deleted every 3 minutes.",
            color=0x00ff00
        )
        await ctx.respond("Message sent successfully.", ephemeral=True)
        
        message = await channel.send(embed=embed)
        await message.pin(reason="Autodelete")

def setup(bot: discord.Bot):
    bot.add_cog(autodelete(bot))