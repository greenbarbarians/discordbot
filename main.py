from discord.ext import commands
import os
import random, requests
import json
import urllib.request

client = commands.Bot(command_prefix='-')

token = os.getenv("TOKEN")

@client.event
async def on_ready():
	print('client ready')

@client.command()
async def brown():
	msg = 'https://cdn.discordapp.com/attachments/263062760424865792/476401246945935380/oops.jpg'
	await client.say(msg)

@client.command()
async def cat():
	print('cats')
	url = "https://api.thecatapi.com/v1/images/search"
	response = urllib.request.urlopen(url)
	result = json.loads(response.read())

	url = result[0]['url']
	await client.say(url)

@client.command()
async def support():
	print('help menu')
	msg = 'Help menu:\n`-help` - Get help\n`-dab` - Get a dab\n`-hentai` - For the good stuff\n`-meme` - Get a dank meme\n`-cat` - Get a picture of a cat\n`-nsfw` - Gwizz\n`-duck` - Duckle\n'
	await client.say(msg)

@client.command()
async def dab():
	print('Dab!')
	msg = '( ͡° ͜ʖ ͡°)'
	await client.say(msg)

@client.command()
async def nsfw():
	print('Gwizz')
	msg = 'Someone say nsfw? I got you https://cdn.discordapp.com/attachments/263062760424865792/532602893287686165/brown_cat.png'
	await client.say(msg)

@client.command()
async def hentai():
	print('Yum time')
	response = requests.get("https://www.reddit.com/r/hentai.json", headers={"User-Agent": "linux:memebot:v1.0.0"})
	page = response.json()
	all_urls = random.choice(page["data"]["children"])["data"]["url"]
	msg = all_urls
	await client.say(msg)

@client.command()
async def duck():
	print('Duck!')
	msg = 'https://giphy.com/gifs/duck-excited-school-krewXUB6LBja'
	await client.say(msg)

@client.command()
async def meme():
	print('Meme time')
	response = requests.get("https://www.reddit.com/r/meme.json", headers={"User-Agent": "linux:memebot:v1.0.0"})
	page = response.json()
	all_urls = random.choice(page["data"]["children"])["data"]["url"]
	msg = all_urls
	await client.say(msg)

client.run(token)
