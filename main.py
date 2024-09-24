import nextcord as nc
from nextcord.ext import commands
from os import getenv
from dotenv import load_dotenv
from utils import Utils

class BotLauncher:
    def __init__(self):
        """Initialise la classe BotLauncher."""
        intents = nc.Intents.all()
        self.bot = commands.Bot(intents=intents)
        
        # Charge tous les cogs depuis le répertoire cogs
        self.load_cogs()

    def load_cogs(self):
        """Charge tous les cogs."""
        for cog in Utils.load_cogs():
            try:
                self.bot.load_extension(cog)
                print(f"Cog chargé : {cog}")
            except Exception as e:
                print(f"Erreur lors du chargement du cog {cog}: {e}")

    def run(self):
        """Lance le bot."""
        load_dotenv()
        token = getenv("TOKEN_DISCORD")
        if not token:
            raise ValueError("Le token Discord n'a pas été trouvé dans les variables d'environnement.")
        self.bot.run(token)

if __name__ == "__main__":
    launcher = BotLauncher()
    launcher.run()