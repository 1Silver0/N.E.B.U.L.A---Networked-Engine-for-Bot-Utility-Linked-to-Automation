import discord
from discord.ext import commands
import aiohttp
import asyncio

timeout = aiohttp.ClientTimeout(total=10)
retries = 3
url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
headers = {"User-Agent": "YOUR_USER_AGENT"}

class Define(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def define(self, ctx, word: str):
        async with aiohttp.ClientSession(timeout=timeout) as session:
            for attempt in range(retries):
                try:
                    async with session.get(url + word.lower(), headers=headers) as resp:
                        resp.raise_for_status()
                        if resp.status != 200:
                            file1 = discord.File("NEBULA/NebulaV1_2/ERROR.png", filename="ERROR.png")
                            embed1 = discord.Embed(description=f"Error (code): **{resp.status}**", color=discord.Color.red())
                            embed1.set_footer(text="N.E.B.U.L.A Operating Systems - Powered by Python")
                            embed1.set_image(url="attachment://ERROR.png")
                            await ctx.send(embed=embed1, file=file1)
                            return
                        data = await resp.json()
                except aiohttp.ClientError as e:
                    if attempt == retries - 1:
                        file2 = discord.File("NEBULA/NebulaV1_2/ERROR.png", filename="ERROR.png")
                        embed2 = discord.Embed(description=f"Error: **{e}**", color=discord.Color.red())
                        embed2.set_footer(text="N.E.B.U.L.A Operating Systems - Powered by Python")
                        embed2.set_image(url="attachment://ERROR.png")
                        await ctx.send(embed=embed2, file=file2)
                        return
                    await asyncio.sleep(1)
        
            if not data or "meanings" not in data[0] or not data[0]["meanings"]:
                file3 = discord.File("NEBULA/NebulaV1_2/ERROR.png", filename="ERROR.png")
                embed3 = discord.Embed(description=f"Error: NoMeaningForWord", color=discord.Color.red())
                embed3.set_footer(text="N.E.B.U.L.A Operating Systems - Powered by Python")
                embed3.set_image(url="attachment://ERROR.png")
                await ctx.send(embed=embed3, file=file3)
                return

            word_text = data[0].get("word", word)
            phonetic = data[0].get("phonetic", "N/A")
            meanings = data[0]["meanings"]

            definition_text = ""
            for meaning in meanings[:3]:
                pos = meaning.get("partOfSpeech", "N/A")
                defs = meaning.get("definitions", [])
                if defs:
                    definition = defs[0].get("definition", "N/A")
                    example = defs[0].get("example", "N/A")
                    definition_text += f"**{pos}**: {definition}\n"
                    if example:
                        definition_text += f"_Example_: {example}\n"
                    definition_text += "\n"
            file4 = discord.File("NEBULA/NebulaV1_2/SUCCESS.png", filename="SUCCESS.png")
            embed4 = discord.Embed(title=f"Definition of {word_text}:", description=definition_text.strip(), color=discord.Color.green())
            embed4.add_field(name="Pronunciation", value=phonetic, inline=False)
            embed4.set_footer(text="N.E.B.U.L.A Operating Systems - Powered by Python")
            embed4.set_image(url="attachment://SUCCESS.png")
            await ctx.send(embed=embed4, file=file4)

async def setup(bot):
    await bot.add_cog(Define(bot))