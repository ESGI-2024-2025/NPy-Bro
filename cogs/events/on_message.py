from nextcord.ext import commands
import nextcord

class OnMessageEventsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: nextcord.Message):
        if (message.author == self.bot.user): return
        print(f"Message reçu : {message.content}")

def setup(bot):
    bot.add_cog(OnMessageEventsCog(bot))