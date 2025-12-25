import discord
from discord.ext import commands
import wikipediaapi
import asyncio

wiki_wiki = wikipediaapi.Wikipedia(language = 'en', user_agent = 'YOUR_USER-AGENT')

class Research(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def research (self, ctx, *, query: str):
        file1 = discord.File("NEBULA/NebulaV1_2/WAIT....png", filename="WAIT....png")
        embed1 = discord.Embed(description="Performing research...", color=discord.Color.yellow())
        embed1.set_footer(text="N.E.B.U.L.A Operating Systems - Powered by Python")
        embed1.set_image(url="attachment://WAIT....png")
        await ctx.send(embed=embed1, file=file1)

        loop = asyncio.get_running_loop()
        page = await loop.run_in_executor(None, wiki_wiki.page, query)

        if not page.exists():
            file2 = discord.File("NEBULA/NebulaV1.1/ERROR.png", filename="ERROR.png")
            embed2 = discord.Embed(description=f"Error: Nothing about {query}", color=discord.Color.red())
            embed2.set_footer(text="N.E.B.U.L.A Operating Systems - Powered by Python")
            embed2.set_thumbnail(url="attachment://ERROR.png")
            await ctx.send(embed=embed2, file=file2)
            return
    
        summary = page.summary[:1000]

        file3 = discord.File("NEBULA/NebulaV1_2/SUCCESS.png", filename="SUCCESS.png")
        embed3 = discord.Embed(title=f"Information about **{query}**:", color=discord.Color.green())
        embed3.add_field(name=f"", value=f"{summary}", inline=False)
        embed3.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/6/63/Wikipedia-logo.png")
        embed3.set_footer(text="N.E.B.U.L.A Operating Systems - Powered by Python")
        embed3.set_image(url="attachment://SUCCESS.png")
        await ctx.send(embed=embed3, file=file3)

async def setup(bot):
    await bot.add_cog(Research(bot))