# a terrible bot for a small server with friends

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
client = commands.Bot(command_prefix='-')
token = os.getenv("TOKEN")


@client.event
async def on_ready():
	client.http2 = aiohttp.ClientSession(headers={"User-Agent": "linux:memebot:v1.0.0"})
	# noinspection PyArgumentList
	await client.change_presence(activity=discord.Game("with Keshin"))
	print('client ready')


# if message contains commands
@client.event
async def on_message(message):
	# don't reply to itself
	if message.author == client.user:
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
	await client.process_commands(message)


# get a mal profile
@client.command()
async def mal(ctx, arg):
	link = 'https://myanimelist.net/profile/' + arg
	await ctx.send(link)


# get a cat picture
@client.command()
async def cat(ctx):
	print('cats')
	async with client.http2.get("https://api.thecatapi.com/v1/images/search") as response:
		result = await response.json()
	url = result[0]['url']
	await ctx.send(url)


# get a meme from /r/okbuddyretard
@client.command()
async def meme(ctx):
	print('Meme time')
	async with client.http2.get("https://www.reddit.com/r/okbuddyretard.json") as response:
		page = await response.json()
	all_urls = random.choice(page["data"]["children"])["data"]["url"]
	msg = all_urls
	await ctx.send(msg)


# on marcus' request
@client.command()
async def hentai(ctx):
	print('Yum time')
	async with client.http2.get("https://www.reddit.com/r/hentai.json") as response:
		page = await response.json()
	all_urls = random.choice(page["data"]["children"])["data"]["url"]
	msg = all_urls
	await ctx.send(msg)


# help menu
@client.command()
async def support(ctx):
	print('help menu')
	msg = 'Help menu:\n`-help` - Get help\n`-dab` - Get a dab\n`-baka` - Baka gif\n`-hentai` - For the good stuff\n`-meme` - Get a dank meme\n`-cat` - Get a picture of a cat\n`-nsfw` - Gwizz\n`-duck` - Duckle\n'
	await ctx.send(msg)


# an excited duck
@client.command()
async def duck(ctx):
	print('duck')
	msg = 'https://giphy.com/gifs/duck-excited-school-krewXUB6LBja'
	await ctx.send(msg)


# baka gif
@client.command()
async def baka(ctx):
	print('baka')
	msg = 'https://media.tenor.com/images/38fff1193d3535d83a3e4d73f032ef61/tenor.gif'
	await ctx.send(msg)


client.run(token)
