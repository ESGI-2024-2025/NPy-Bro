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

        embed = nc.Embed(colour=0xffffff,
                        title="Membres du Notion",
                        url="https://living-jupiter-d3e.notion.site/Cours-et-Devoirs-fff109d1eb40810cb97cf5029bec4b1c")

        for m in members["results"]:

            if m["type"] != "person":
                continue

            embed.add_field(name=m["name"],value=f"*{m["person"]["email"]}*",inline=False)

        embed.set_thumbnail("https://upload.wikimedia.org/wikipedia/commons/4/45/Notion_app_logo.png")
        await interaction.send(embed=embed)


def setup(bot):
    load_dotenv()
    NOTION = getenv("TOKEN_NOTION")
    client = notion_client.AsyncClient(auth=NOTION)
    bot.add_cog(Notion(bot,client))

