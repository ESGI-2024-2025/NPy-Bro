from nextcord.ext import commands

class OnReadyEventsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Bot connecté en tant que {self.bot.user}")

def setup(bot):
    bot.add_cog(OnReadyEventsCog(bot))