from discord.ext import commands


class MAL(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # get a mal profile
    @commands.command()
    async def mal(self, ctx, arg):
        print('mal profile')
        link = 'https://myanimelist.net/profile/' + str(arg)
        await ctx.send(link)

    # mal anime list
    @commands.command()
    async def malanime(self, ctx, arg):
        print('mal anime')
        link = 'https://myanimelist.net/animelist/' + arg
        await ctx.send(link)

    # mal manga list
    @commands.command()
    async def malmanga(self, ctx, arg):
        print('mal manga')
        link = 'https://myanimelist.net/mangalist/' + arg
        await ctx.send(link)


def setup(bot):
    bot.add_cog(MAL(bot))
