import discord
from discord.ext import commands
import sqlite3
import aiosqlite

MEMORY = "YOUR_STORAGE_FILE"

class Forget(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def forget(self, ctx, key):

        async with aiosqlite.connect(MEMORY) as db:
            await db.execute("DELETE FROM memory WHERE user=? AND key=?", (str(ctx.author.id), key))
            await db.commit()

        if db.rowcount == 0:
            file1 = discord.File("NEBULA/NebulaV1_2/ERROR.png", filename="ERROR.png")
            embed1 = discord.Embed(description=f"Error: NothingNamedWord", color=discord.Color.red())
            embed1.set_footer(text="N.E.B.U.L.A Operating Systems - Powered by Python")
            embed1.set_image(url="attachment://ERROR.png")
            await ctx.send(embed=embed1, file=file1)
        else:
            file2 = discord.File("NEBULA/NebulaV1_2/SUCCESS.png", filename="SUCCESS.png")
            embed2 = discord.Embed(description=f"**{key}** was forgotten", color=discord.Color.green())
            embed2.set_footer(text="N.E.B.U.L.A Operating Systems - Powered by Python")
            embed2.set_image(url="attachment://SUCCESS.png")
            await ctx.send(embed=embed2, file=file2)

async def setup(bot):
    await bot.add_cog(Forget(bot))