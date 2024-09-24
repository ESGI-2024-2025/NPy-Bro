import notion_client
import nextcord as nc
from nextcord.ext import commands
from os import getenv
from dotenv import load_dotenv

class Notion(commands.Cog):

    def __init__(self, bot, notion) -> None:
        self.bot = bot
        self.notion_client = notion

    @nc.slash_command(description="Commandes Notion")
    async def notion(self, interaction: nc.Interaction):
        pass

    @notion.subcommand(description="Obtenir les membres du Notion")
    async def membres(self, interaction: nc.Interaction):
        members = await self.notion_client.users.list()
        print(members)
        await interaction.send("Les membres sont affichés en console")


def setup(bot):
    load_dotenv()
    NOTION = getenv("TOKEN_NOTION")
    client = notion_client.Client(auth=NOTION)
    bot.add_cog(Notion(bot,client))

