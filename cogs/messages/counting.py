import os
import discord
from discord.ext import commands
import ezcord
from pymongo import MongoClient
from dotenv import load_dotenv
from cogs.messages.CountingData import CountingData 

load_dotenv()

MONGO_URI = os.getenv("MONGODB_URI")
client = MongoClient(MONGO_URI)

db = client['Bot_data']
count_collection = db['counting']

class CounterCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.counter_channel = # Your Channel ID
        self.counter_data = CountingData()
        self.count = self.counter_data.get_count()

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id != self.counter_channel:
            return
        if message.author.bot:
            return
        try:
            number = int(message.content)
            if number == self.count + 1:
                self.count += 1
                self.counter_data.count = self.count
                self.counter_data.save() 
                await message.add_reaction("✅")
            else:
                await message.delete()
        except ValueError:
            await message.delete()

def setup(bot):
    bot.add_cog(CounterCog(bot))