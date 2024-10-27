# Imports
import discord
import os
from dotenv import load_dotenv # Run 'pip install python-dotenv' in the terminal

load_dotenv()

intents = discord.Intents.default()  # Sets the Intents for the Bot
intents.message_content = True  # Enable additional intents if needed

status = discord.Status.online  # Sets the status to online, can also be set to dnd, idle, offline, invisible, or streaming.
activity = discord.Activity(type=discord.ActivityType.custom, name="😀 Bot Status")  # Sets the activity

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
    # Recursively loads all Cogs from the 'cogs' folder and its subfolders
    for root, dirs, files in os.walk("cogs"):
        for filename in files:
            if filename.endswith(".py"):
                # Creates the module path for the Cog (e.g., 'cogs.subfolder.cogname')
                cog_path = os.path.join(root, filename[:-3]).replace(os.sep, ".")
                try:
                    bot.load_extension(cog_path)
                    print(f"Loaded cog: {cog_path}")
                except Exception as e:
                    print(f"Error loading cog {cog_path}: {e}")


bot.run(os.getenv("TOKEN"))  # Ensure TOKEN is set in your .env file
