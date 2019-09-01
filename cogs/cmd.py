from discord.ext import commands
import random


class Cmd(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	# an excited duck
	@commands.command()
	async def duck(self, ctx):
		print('duck')
		msg = 'https://giphy.com/gifs/duck-excited-school-krewXUB6LBja'
		await ctx.send(msg)

	# baka gif
	@commands.command()
	async def baka(self, ctx):
		print('baka')
		msg = 'https://media.tenor.com/images/38fff1193d3535d83a3e4d73f032ef61/tenor.gif'
		await ctx.send(msg)

	# get a cat picture
	@commands.command()
	async def cat(self, ctx):
		print('cats')
		async with self.bot.http2.get("https://api.thecatapi.com/v1/images/search") as response:
			result = await response.json()
		url = result[0]['url']
		await ctx.send(url)

	# on marcus' request
	@commands.command()
	async def hentai(self, ctx):
		print('Yum time')
		async with self.bot.http2.get("https://www.reddit.com/r/hentai.json") as response:
			page = await response.json()
		all_urls = random.choice(page["data"]["children"])["data"]["url"]
		msg = all_urls
		await ctx.send(msg)

	# get a meme from /r/okbuddyretard
	@commands.command()
	async def meme(self, ctx):
		print('Meme time')
		async with self.bot.http2.get("https://www.reddit.com/r/okbuddyretard.json") as response:
			page = await response.json()
		all_urls = random.choice(page["data"]["children"])["data"]["url"]
		msg = all_urls
		await ctx.send(msg)


def setup(bot):
	bot.add_cog(Cmd(bot))
