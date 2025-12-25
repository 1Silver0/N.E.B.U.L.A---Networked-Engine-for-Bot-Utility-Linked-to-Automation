import discord
from discord.ext import commands
import aiohttp

API_KEY = "YOUR_API-KEY"
timeout = aiohttp.ClientTimeout(total=10)

class News(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def news(self, ctx, country: str, category: str = "general"):
        url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey=" + API_KEY
        if category:
            url += f"&category={category}"
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(url) as resp:
                if resp.status != 200:
                    file = discord.File("NEBULA/NebulaV1.1/ERROR.png", filename="ERROR.png")
                    embed1 = discord.Embed(description=f"Error: **{resp.status}**", color=discord.Color.red())
                    embed1.set_footer(text="N.E.B.U.L.A Operating Systems - Powered by Python")
                    embed1.set_thumbnail(url="attachment://ERROR.png")
                    await ctx.send(embed=embed1, file=file)
                    return

                data = await resp.json()
        articles = data.get("articles", [])[:5]
        if not articles:
            file = discord.File("NEBULA/NebulaV1.1/ERROR.png", filename="ERROR.png")
            embed2 = discord.Embed(description=f"Error: NoNewsAbout**{category}**In**{country}**", color=discord.Color.red())
            embed2.set_footer(text="N.E.B.U.L.A Operating Systems - Powered by Python")
            embed2.set_thumbnail(url="attachment://ERROR.png")
            await ctx.send(embed=embed2, file=file)
            return
        
        file3 = discord.File("NEBULA/NebulaV1_2/SUCCESS.png", filename="SUCCESS.png")
        embed3 = discord.Embed(description=f"News about **{category}** in **{country}**:", color=discord.Color.green())
        embed3.set_footer(text="N.E.B.U.L.A Operating Systems - Powered by Python")
        embed3.set_image(url="attachment://SUCCESS.png")
        await ctx.send(embed=embed3, file=file3)

        message = ""
        for a in articles:
            title = a.get("title", "No title")
            desc = a.get("description", "No description")
            url = a.get("url", "No URL")
            img = a.get("urlToImage", "No image")
            source = a.get("source", {}).get("name", "Unknown author")

            embed4 = discord.Embed(title=title, description=desc, url=url, color=discord.Color.green())
            if img:
                embed4.set_image(url=img)
            embed4.set_author(name=source)
            embed4.set_footer(text="N.E.B.U.L.A Operating Systems - Powered by Python")
            await ctx.send(embed=embed4)

async def setup(bot):
    await bot.add_cog(News(bot))