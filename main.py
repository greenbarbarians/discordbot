import discord
from discord.ext import commands
import os
from keep_alive import keep_alive
import random, requests

client = discord.Client()

client = commands.Bot("-")

@client.event
async def on_ready():
	print("I'm in")
	print(client.user)

class Main_Commands():
	global bot
	def __init__(self, bot):
		self.bot = bot

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('-help'):
		print('help menu')
		msg = 'Help menu:\n`-help` - Get help\n`-dab` - Get a dab\n`-hentai` - For the good stuff\n`-meme` - Get a dank meme\n'.format(message)
		await client.send_message(message.channel, msg)

	if message.content.startswith('-hello'):
		print('Hello')
		msg = 'Hello {0.author.mention}'.format(message)
		await client.send_message(message.channel, msg)

	if message.content.startswith('-dab'):
		print('Dab!')
		msg = '( ͡° ͜ʖ ͡°)'.format(message)
		await client.send_message(message.channel, msg)
		
	if message.content.startswith('Keep Yourself Safe'):
		print('Bungus response')
		msg = 'Thanks Bungus for keeping us safe'.format(message)
		await client.send_message(message.channel, msg)

	if message.content.startswith('Ollie is so dumb'):
		msg = 'Yes, he is.'.format(message)
		await client.send_message(message.channel, msg)
	
	if 'nsfw' in message.content:
		print('Gwizz')
		msg = 'Someone say nsfw? I got you https://cdn.discordapp.com/attachments/263062760424865792/532602893287686165/brown_cat.png'.format(message)
		await client.send_message(message.channel, msg)

	if '-hentai' in message.content:
		print('Yum time')
		response = requests.get("https://www.reddit.com/r/hentai.json", headers={"User-Agent": "linux:memebot:v1.0.0"})
		page = response.json()
		all_urls = random.choice(page["data"]["children"])["data"]["url"]
		# msg = 'all_urls'.format(message)
		await client.send_message(message.channel, all_urls)

	if 'join' in message.content:
		print('Join')
		msg = 'No flip off'.format(message)
		await client.send_message(message.channel, msg)

	if 'furry' in message.content:
		print('Sad furry picture')
		msg = 'I lost my family in the great gamer wars https://cdn.discordapp.com/attachments/263062760424865792/530898062990770192/Justice.jpg'.format(message)
		await client.send_message(message.channel, msg)

	if 'gamer' in message.content:
		print('Sad furry picture')
		msg = 'I lost my family in the great gamer wars https://cdn.discordapp.com/attachments/263062760424865792/530898062990770192/Justice.jpg'.format(message)
		await client.send_message(message.channel, msg)

	if 'duck' in message.content:
		print('Duck!')
		msg = 'https://giphy.com/gifs/duck-excited-school-krewXUB6LBja'.format(message)
		await client.send_message(message.channel, msg)

	if 'cat' in message.content:
		print('Brown cat')
		msg = 'https://cdn.discordapp.com/attachments/263062760424865792/476401246945935380/oops.jpg'.format(message)
		await client.send_message(message.channel, msg)

	if '-meme' in message.content:
		print('Meme time')
		response = requests.get("https://www.reddit.com/r/meme.json", headers={"User-Agent": "linux:memebot:v1.0.0"})
		page = response.json()
		all_urls = random.choice(page["data"]["children"])["data"]["url"]
		# msg = 'all_urls'.format(message)
		await client.send_message(message.channel, all_urls)

keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
