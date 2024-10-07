from nextcord.ext import commands

class OnReactionEventsCog(commands.Cog):
    def __init__(self, bot, reaction_message_id, channel_send_id):
        self.bot = bot
        self.reaction_message_id = reaction_message_id
        self.channel_send_id = channel_send_id

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, reaction):
        
        channel_send = await self.bot.fetch_channel(self.channel_send_id)

        if reaction.message_id == self.reaction_message_id and reaction.emoji.name == "✅":
            await channel_send.send(f"`{reaction.member} souhaite voir son compte créé !`")
        
        

def setup(bot):
    bot.add_cog(OnReactionEventsCog(bot, 1292516023932682291, 1288144366820397230))