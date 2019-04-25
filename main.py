from discord.ext import commands
import discord
import os
import random
import aiohttp
from os.path import join, dirname
from dotenv import load_dotenv

# load .env
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# client settings
bot = commands.Bot(command_prefix='-')
token = os.getenv("TOKEN")

# indicate cogs
initial_extensions = ['cogs.mal','cogs.react']

# load cogs
if __name__ == '__main__':
	for extension in initial_extensions:
		bot.load_extension(extension)


# startup
@bot.event
async def on_ready():
	bot.http2 = aiohttp.ClientSession(headers={"User-Agent": "linux:memebot:v1.0.0"})
	# noinspection PyArgumentList
	await bot.change_presence(activity=discord.Game("with Keshin"))
	print('client ready')


# get a cat picture
@bot.command()
async def cat(ctx):
	print('cats')
	async with bot.http2.get("https://api.thecatapi.com/v1/images/search") as response:
		result = await response.json()
	url = result[0]['url']
	await ctx.send(url)


# get a meme from /r/okbuddyretard
@bot.command()
async def meme(ctx):
	print('Meme time')
	async with bot.http2.get("https://www.reddit.com/r/okbuddyretard.json") as response:
		page = await response.json()
	all_urls = random.choice(page["data"]["children"])["data"]["url"]
	msg = all_urls
	await ctx.send(msg)


# on marcus' request
@bot.command()
async def hentai(ctx):
	print('Yum time')
	async with bot.http2.get("https://www.reddit.com/r/hentai.json") as response:
		page = await response.json()
	all_urls = random.choice(page["data"]["children"])["data"]["url"]
	msg = all_urls
	await ctx.send(msg)


# help menu
@bot.command()
async def support(ctx):
	print('help menu')
	msg = 'Help menu:\n`-help` - Get help\n`-dab` - Get a dab\n`-baka` - Baka gif\n`-hentai` - For the good stuff\n`-meme` - Get a dank meme\n`-cat` - Get a picture of a cat\n`-nsfw` - Gwizz\n`-duck` - Duckle\n`-mal` - View MyAnimeList profile\n`-malanime` - View MAL anime list\n`-malmanga` - View MAL manga list\n'
	await ctx.send(msg)


# an excited duck
@bot.command()
async def duck(ctx):
	print('duck')
	msg = 'https://giphy.com/gifs/duck-excited-school-krewXUB6LBja'
	await ctx.send(msg)


# baka gif
@bot.command()
async def baka(ctx):
	print('baka')
	msg = 'https://media.tenor.com/images/38fff1193d3535d83a3e4d73f032ef61/tenor.gif'
	await ctx.send(msg)


bot.run(token)
