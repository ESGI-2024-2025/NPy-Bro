import nextcord as nc
from nextcord.ext import commands

class sendGithub(commands.Cog):

    def __init__(self, bot) -> None:
        self.bot = bot

    @nc.slash_command(description="Envoie le Github avec les corrections")
    async def github(self, interaction: nc.Interaction):
        await interaction.send("np bro, t'as tout ici : https://github.com/smoothwastaken/ESGI/tree/master")

def setup(bot):
    bot.add_cog(sendGithub(bot))
