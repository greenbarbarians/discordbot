import discord
import os
from keep_alive import keep_alive

client = discord.Client()


@client.event
async def on_ready():
  print("I'm in")
  print(client.user)


@client.event
async def on_message(message):
	# we do not want the bot to reply to itself
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
    
keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
