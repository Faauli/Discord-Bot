import discord


class embeds(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot
      
    #Add code

def setup(bot: discord.Bot):
    bot.add_cog(embeds(bot))
