from discord.ext import commands


class Help(commands.Cog):
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
		`-reddit [subreddit name]` - Get a random hot post from a subreddit
		
		The bot also has various reaction commands that are not detailed here.
		'''
		await ctx.send(msg)


def setup(bot):
	bot.add_cog(Help(bot))
