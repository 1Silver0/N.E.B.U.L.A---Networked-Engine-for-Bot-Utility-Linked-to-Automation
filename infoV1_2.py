import discord
from discord.ext import commands

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def info(self, ctx):
        embed1 = discord.Embed(title="N.E.B.U.L.A - Networked Engine for Bot Utility Linked to Automation", description="N.E.B.U.L.A is the evolved successor to Nova, a highly intelligent, serious AI assistant. Where Nova sparked creativity, N.E.B.U.L.A delivers precision, efficiency, and advanced analysis. It observes, remembers, and guides with authority, making every interaction purposeful.", color=discord.Color.purple())

        embed2 = discord.Embed(title="Changelog", color=discord.Color.purple())
        embed2.add_field(name="V1.0", value="Moved all of Nova's commands into N.E.B.U.L.A's systems, changed all responses to match N.E.B.U.L.A's more precise personality.", inline=False)
        embed2.add_field(name="V1.1", value="Added personal Box for users (.openbox, .setbox).\nAdded .news command.\nN.E.B.U.L.A no longer uses the 'requests' module and normal SQLite, instead it now uses 'aiohttp' and 'aiosqlite' modules for a more asynchronous flow\nN.E.B.U.L.A's name is now an acronym that stands for 'Networked Engine for Bot Utility Linked to Automation'\nMade small changes to the '.status' command\nAdded .define command (finds definition of a word)\nAdded encryption tools (.encrypt, .decrypt)\nAdded images for embeds", inline=False)
        embed2.add_field(name="V1.2", value="Added unit converter (.unitconvert)\nAdded anvanced help command (.nhelp)\nUpdated .unitconvert with dropdowns for selection\nMade changes to startup sequence\nMade changes to shutdown sequence", inline=False)
        embed2.set_footer(text="N.E.B.U.L.A Operating Systems - Powered by Python")

        await ctx.send(embed=embed1)
        await ctx.send(embed=embed2)

async def setup(bot):
    await bot.add_cog(Info(bot))