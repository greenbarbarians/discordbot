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
		`-dab` - Get a dab
		`-baka` - Baka gif
		`-hentai` - For the good stuff
		`-meme` - Get a dank meme
		`-cat` - Get a picture of a cat
		`-duck` - Get a good duck picture
		`-mal` - View MyAnimeList profile
		`-malanime` - View MAL anime list
		`-malmanga` - View MAL manga list
		
		The bot also has various reaction commands that are not detailed here.
		'''
		await ctx.send(msg)

def setup(bot):
	bot.add_cog(help(bot))
