import discord
from discord.ext import commands
import os
from keep_alive import keep_alive

client = discord.Client()

client = commands.Bot(command_prefix="-")


@client.event
async def on_ready():
	print("I'm in")
	print(client.user)


@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('-hello'):
		msg = 'Hello {0.author.mention}'.format(message)
		await client.send_message(message.channel, msg)

	if message.content.startswith('-dab'):
		msg = '( ͡° ͜ʖ ͡°)'.format(message)
		await client.send_message(message.channel, msg)
		
	if message.content.startswith('Keep Yourself Safe'):
		msg = 'Thanks Bungus for keeping us safe'.format(message)
		await client.send_message(message.channel, msg)

	if message.content.startswith('Ollie is so dumb'):
		msg = 'Yes, he is.'.format(message)
		await client.send_message(message.channel, msg)
	
	if 'nsfw' in message.content:
		print('Keyword found in message')
		msg = 'https://cdn.discordapp.com/attachments/263062760424865792/532602893287686165/brown_cat.png'.format(message)
		await client.send_message(message.channel, msg)

keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
