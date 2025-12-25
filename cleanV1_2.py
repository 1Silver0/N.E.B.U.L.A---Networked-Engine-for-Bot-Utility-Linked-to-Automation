import discord
from discord.ext import commands

ID = "YOUR_DISCORD_USER-ID_HERE"

class Clean(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def clean(self, ctx, channel: discord.TextChannel, amount: int):
        if ctx.author.id != ID:
            file1 = discord.File("NEBULA/NebulaV1_2/ERROR.png", filename="ERROR.png")
            embed1 = discord.Embed(description="Use of command only allowed by Silver", color=discord.Color.red())
            embed1.set_footer(text="N.E.B.U.L.A Operating Systems - Powered by Python")
            embed1.set_thumbnail(url="attachment://ERROR.png")
            await ctx.send(embed=embed1, file=file1)
            return
        
        def not_pinned(m):
            return not m.pinned
        
        deleted = await channel.purge(limit=amount, check=not_pinned)

        file2 = discord.File("NEBULA/NebulaV1_2/SUCCESS.png", filename="SUCCESS.png")
        embed2 = discord.Embed(description=f"Deleting {len(deleted)} messages...", color=discord.Color.green())
        embed2.set_footer(text="N.E.B.U.L.A Operating Systems - Powered by Python")
        embed2.set_image(url="attachment://SUCCESS.png")
        await ctx.send(embed=embed2, file=file2, deleted_after=5)

async def setup(bot):
    await bot.add_cog(Clean(bot))