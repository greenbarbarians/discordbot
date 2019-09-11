from discord.ext import commands


class React(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        # don't reply to itself
        if message.author == self.bot.user:
            return
        # gwizz
        if 'nsfw' in message.content:
            print('Gwizz')
            msg = 'Someone say nsfw? I got you https://cdn.discordapp.com/attachments/263062760424865792/532602893287686165/brown_cat.png'
            await message.channel.send(msg)
        # brown cat
        elif 'brown cat' in message.content:
            print('brown cat')
            msg = 'https://cdn.discordapp.com/attachments/263062760424865792/476401246945935380/oops.jpg'
            await message.channel.send(msg)
        # black cat
        elif 'black cat' in message.content:
            print('black cat')
            msg = 'https://cdn.discordapp.com/attachments/263062760424865792/617299515069956096/image0.jpg'
            await message.channel.send(msg)
        # toontown
        elif 'toontown' in message.content:
            print('yikes')
            msg = 'Someone say loser? https://cdn.discordapp.com/attachments/565499249316462592/565507485788536832/ttr-screenshot-_Brother2Band2Bsister_-Mon-Aug-18-18-40-21-2014-107256.png'
            await message.channel.send(msg)
        # holy image
        elif 'clembo' in message.content:
            print('clembo')
            msg = 'amen https://cdn.discordapp.com/attachments/293807439713927169/565625753366954044/lugi.gif'
            await message.channel.send(msg)
        # clean
        elif 'clean' in message.content:
            print('clean')
            msg = 'https://cdn.discordapp.com/attachments/263062760424865792/600429304857493507/unknown.png'
            await message.channel.send(msg)
        # dumbass
        elif 'nathan' in message.content:
            print('nathan is epic')
            msg = 'https://cdn.discordapp.com/attachments/447136986277347339/621380608047710208/Nathan_as_a_rabbit.jpg'
            await message.channel.send(msg)


def setup(bot):
    bot.add_cog(React(bot))
