import nextcord as nc
from nextcord.ext import commands

class sendMeme(commands.Cog):

    def __init__(self, bot) -> None:
        self.bot = bot

    @nc.slash_command(description="np bro")
    async def np_bro(self, interaction: nc.Interaction):
        await interaction.send("np bro")

def setup(bot):
    bot.add_cog(sendMeme(bot))
