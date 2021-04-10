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
		elif 'brown' in message.content:
			print('brown cat')
			msg = 'https://cdn.discordapp.com/attachments/263062760424865792/476401246945935380/oops.jpg'
			await message.channel.send(msg)
		# black cat
		elif 'black' in message.content:
			print('black cat')
			msg = 'https://cdn.discordapp.com/attachments/293807439713927169/565473888524304404/image0.jpg'
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
		# bopping cat
		elif "-play" or "!play" or ".play" or "_play" in message.content:
			print('music cat')
			msg= 'https://media.discordapp.net/attachments/453830474339450905/739205450666606652/image0-37-1.gif'
			await message.channel.send(msg)
		# lol
		elif "lol" or "Lol" or "LOL" in message.content:
			print("lol")
			msg= "Haha! LOL! :-)"
			await message.channel.send(msg)
		# operation piss off ollie
		elif "mukbang" or "Mukbang" or "Nikocado" or "nikocado" in message.content:
			print("Nick")
			msg= "https://cdn.discordapp.com/attachments/688778639700918373/826771127589666816/unknown.png"
			await message.channel.send(msg)
		# monkey space
		elif "nasa" or "Nasa" or "NASA" or "spaceship" in message.content:
			print("monkey")
			msg= "https://images-ext-2.discordapp.net/external/u-PXAjyoEwDerRvcHgcAlWSjd_UwbVw4zCesYXjUYOI/https/i.imgur.com/PMwhpZF.mp4"
			await message.channel.send(msg)
		# Big Floppa
		elif "Big Floppa" or "big floppa" or "Floppa" or "floppa" or "Fanta" or "Gregory" or "Caracal" or "gregory" or "caracal"
			print("floppa")
			msg= "Big Floppa https://cdn.discordapp.com/attachments/688778639700918373/830396177727750164/caracal-gregory-meme.png"
			await message.channel.send(msg)

def setup(bot):
	bot.add_cog(React(bot))
