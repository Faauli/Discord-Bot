import os
import discord
from pymongo import MongoClient
from dotenv import load_dotenv
import ezcord

load_dotenv()

MONGO_URI = os.getenv("MONGODB_URI")
client = MongoClient(MONGO_URI)

db = client['Bot_data']
count_collection = db['counting']

class CountingData(ezcord.Cog):
    def __init__(self, count=0):
        self.count = count

    def save(self):
        count_document = {
            "count": self.count
        }
        count_collection.update_one(
            {},
            {"$set": count_document},
            upsert=True
        )

    def get_count(self):
        count_data = count_collection.find_one({})
        if count_data:
            return count_data.get("count", 0)
        return 0

def setup(bot: discord.Bot):
    bot.add_cog(CountingData(bot))