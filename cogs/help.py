from discord.ext import commands


class help(commands.Cog):
	def __init__(self, bot):
		self.bot = bot


	# help menu
	@commands.command()
	async def help(self, ctx):
		print('help menu')
		msg = '''
		\nHelp menu:
		`-help` - Get help
		`-baka` - Baka gif
		`-hentai` - For the good stuff
		`-meme` - Get a dank meme
		`-cat` - Get a picture of a cat
		`-duck` - Get a good duck picture
		`-mal [username]` - View MyAnimeList profile
		`-malanime [username]` - View MAL anime list
		`-malmanga [username]` - View MAL manga list
		`-join` - Join a VC (you don't need to do this all the time, you can just use `-play` directly - this primes it - please don't do this too much as it will kill my server)
		`-volume [1-100]` - Change the volume
		`-play [youtube link]` - Play music
		`-stop` - Stop the bot
		The bot also has various reaction commands that are not detailed here.
		'''
		await ctx.send(msg)

def setup(bot):
	bot.add_cog(help(bot))
