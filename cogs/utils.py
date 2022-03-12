from discord.ext.commands import Cog, command

class Utilities(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name="ping")
    async def ping(self, ctx):
        await ctx.send(f'Pong! `{(round(self.bot.latency * 1000))}ms` :ping_pong:')

    @command(name="say", aliases=["echo", "ecchi"])
    async def echo(self, ctx, *, msg):
        await ctx.send(f'```\n{msg}\n```')

def setup(bot):
    bot.add_cog(Utilities(bot))