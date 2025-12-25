import discord
from discord.ext import commands
import aiosqlite

class Openbox(commands.Cog): # BROKEN, W.I.P
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def openbox(self, ctx, password):

        async with aiosqlite.connect("nbsV1.1.db") as db:
            async with db.execute("SELECT content FROM passwords WHERE id=? AND passwords=?"), (str(ctx.author.id), password) as cursor:
                result = await cursor.fetchone()

        if result:
            file1 = discord.File("NEBULA/NebulaV1_2/SUCCESS.png", filename="SUCCESS.png")
            embed1 = discord.Embed(title="Your Box", color=discord.Color.green())
            embed1.add_field(name="Content", value=result[0], inline=False)
            embed1.set_footer(text="N.E.B.U.L.A Operating Systems - Powered by Python")
            embed1.set_image(url="attachment://SUCCESS.png")
            member = await ctx.guild.fetch_member(ctx.author.id)
            await member.send(embed=embed1, file=file1)
        else:
            file2 = discord.File("NEBULA/NebulaV1.2/ERROR.png", filename="ERROR.png")
            embed2 = discord.Embed(description="Error: NoBox", color=discord.Color.red())
            embed2.set_footer(text="N.E.B.U.L.A Operating Systems - Powered by Python")
            embed2.set_thumbnail(url="attachment://ERROR.png")
            await ctx.send(embed=embed2, file=file2)

async def setup(bot):
    await bot.add_cog(Openbox(bot))