import discord


class template(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot
      
    #Add code

def setup(bot: discord.Bot):
    bot.add_cog(template(bot))
