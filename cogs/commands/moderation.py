import nextcord as nc
from nextcord.ext import commands

class Moderation(commands.Cog):

    def __init__(self, bot) -> None:
        self.bot = bot

    @nc.slash_command(description="Envoi de l'agenda de la semaine")
    async def clear(self, interaction: nc.Interaction,
        nombre:int = nc.SlashOption(required=True,min_value=1,max_value=100)
        ):
        
        if not interaction.user.guild_permissions.manage_messages:
            await interaction.send("Wesh tu tentes quoi là ?? T'as pas les perms.")
            return 1
        
        await interaction.channel.purge(limit=nombre)
        await interaction.send("C'est clean bg :ok_hand:",ephemeral=True)


def setup(bot):
    bot.add_cog(Moderation(bot))
