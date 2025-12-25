import discord
from discord.ext import commands

class Calc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def calc(self, ctx, n1: float, o, n2: float):
        
        if o == "+":
            result = n1 + n2
        elif o == "-":
            result = n1 - n2
        elif o == "*":
            result = n1 * n2
        elif o == "/":
            if n2 == 0:
                file1 = discord.File("NEBULA/NebulaV1_2/ERROR.png", filename="ERROR.png")
                embed1 = discord.Embed(description="Error: DivisionWithZeroAttempt", color=discord.Color.red())
                embed1.set_footer(text="N.E.B.U.L.A Operating Systems - Powered by Python")
                embed1.set_thumbnail(url="attachment://ERROR.png")
                return await ctx.send(embed=embed1, file=file1)
            result = n1 / n2
        else:
            file2 = discord.File("NEBULA/NebulaV1_2/ERROR.png", filename="ERROR.png")
            embed2 = discord.Embed(description="Error: InvalidOperation", color=discord.Color.red())
            embed2.set_footer(text="N.E.B.U.L.A Operating Systems - Powered by Python")
            embed2.set_thumbnail(url="attachment://ERROR.png")
            await ctx.send(embed=embed2, file=file2)

        file3 = discord.File("NEBULA/NebulaV1_2/SUCCESS.png", filename="SUCCESS.png")
        embed3 = discord.Embed(title="Result:", description=f"{result}", color=discord.Color.green())
        embed3.set_footer(text="N.E.B.U.L.A Operating Systems - Powered by Python")
        embed3.set_image(url="attachment://SUCCESS.png")
        await ctx.send(embed=embed3, file=file3)

async def setup(bot):
   await bot.add_cog(Calc(bot))