import discord
from discord.ext import commands
import aiosqlite

MEMORY = "YOUR_STORAGE_FILE"

class Recall(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def recall(self, ctx, key):

        async with aiosqlite.connect(MEMORY) as db:
            async with db.execute("SELECT content FROM memory WHERE user=? AND key=?", (str(ctx.author.id), key)) as cursor:
                result = await cursor.fetchone()

        if result:
            file1 = discord.File("NEBULA/NebulaV1_2/SUCCESS.png", filename="SUCCESS.png")
            embed1 = discord.Embed(title=f"{key}", description=f"{result[0]}", color=discord.Color.green())
            embed1.set_footer(text="N.E.B.U.L.A Operating Systems - Powered by Python")
            embed1.set_image(url="attachment://SUCCESS.png")
            await ctx.send(embed=embed1, file=file1)
        else:
            file2 = discord.File("NEBULA/NebulaV1_2/ERROR.png", filename="ERROR.png")
            embed2 = discord.Embed(description=f"Error: NothingNamed**{key}**", color=discord.Color.red())
            embed2.set_footer(text="N.E.B.U.L.A Operating Systems - Powered by Python")
            embed2.set_thumbnail(url="attachment://ERROR.png")
            await ctx.send(embed=embed2, file=file2)

async def setup(bot):
    await bot.add_cog(Recall(bot))