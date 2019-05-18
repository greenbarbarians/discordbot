from discord.ext import commands
import discord
import os
import aiohttp
from os.path import join, dirname
from dotenv import load_dotenv

# load .env
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# client settings
bot = commands.Bot(command_prefix='-')
bot.remove_command('help')
token = os.getenv("TOKEN")

# cog loading
initial_extensions = ['cogs.mal', 'cogs.react', 'cogs.cmd', 'cogs.help']
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


bot.run(token)
