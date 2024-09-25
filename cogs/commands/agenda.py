import nextcord as nc
from nextcord.ext import commands
import os
import time

class sendAgenda(commands.Cog):

    def __init__(self, bot) -> None:
        self.bot = bot
        
    def fetch_agenda(self):
        raw_agenda = os.system("myges agenda")
        return raw_agenda
    
    def format_agenda(self, agenda: str) -> dict:
        print(agenda)

    @nc.slash_command(description="Envoi de l'agenda de la semaine")
    async def agenda(self, interaction: nc.Interaction):
        await interaction.send("np bro, je suis dessus là ça arrive la team, un jour challah elle marchera", ephemeral=True)
        agenda = self.fetch_agenda()
        self.format_agenda(agenda)

def setup(bot):
    bot.add_cog(sendAgenda(bot))
