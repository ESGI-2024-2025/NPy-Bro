import nextcord as nc
from nextcord.ext import commands
from os import listdir, getenv
from dotenv import load_dotenv
from utils import Utils

bot = commands.Bot(intents=nc.Intents.all())

@bot.event
async def on_ready():
    """Execute when the bot is connected.
    """
    print("Bot is connected.")

bot.load_extensions(Utils.load_cogs())

def connect(bot):
    load_dotenv()
    TOKEN = getenv("TOKEN_DISCORD")
    bot.run(TOKEN)

connect(bot)