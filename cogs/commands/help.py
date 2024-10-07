import nextcord as nc
from nextcord.ext import commands
from os import listdir

class helpMessage(commands.Cog):

    def __init__(self, bot) -> None:
        self.bot = bot

    @nc.slash_command(description="Envoie la liste des commandes disponibles")
    async def help(self, interaction: nc.Interaction):
        
        files = (f[:-3] for f in listdir("cogs/commands") if f.endswith(".py"))

        await interaction.send("Voici la liste des commandes disponibles : " + ", ".join(files))

def setup(bot):
    bot.add_cog(helpMessage(bot))
