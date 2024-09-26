import discord
import os
from dotenv import load_dotenv

intents = discord.Intents.default()
status = discord.Status.online
activity = discord.Activity(type=discord.ActivityType.custom, name="😀 Bot Status")

bot = discord.Bot(
                  intents=intents,
                  status=status,
                  activity=activity
                 )


@bot.event
async def on_ready():
    print("----------------------------------")
    print(f"{bot.user} ist online")
    print("----------------------------------")


if __name__ == "__main__":
    for filename in os.listdir("cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")

    load_dotenv()
    bot.run(os.getenv("TOKEN"))
