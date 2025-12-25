import discord
from discord.ext import commands
import aiosqlite

class Expense(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def expense(self, ctx, category: str, price: float):
        async with aiosqlite.connect("YOUR_STORAGE_FILE") as db:
            await db.execute("CREATE TABLE IF NOT EXISTS memory (id INTEGER PRIMARY KEY AUTOINCREMENT, user TEXT, category TEXT, price REAL, type TEXT)")
            await db.execute("INSERT INTO memory (user, category, price, type) VALUES (?, ?, ?, 'expense')",(str(ctx.author.id), category, price))
            await db.commit()

        file = discord.File("NEBULA/NebulaV1_2/SUCCESS.png", filename="SUCCESS.png")
        embed = discord.Embed(description=f"**Expense: {category}** saved at the price of **{price}**", color=discord.Color.green())
        embed.set_footer(text="N.E.B.U.L.A Operating Systems - Powered by Python")
        embed.set_image(url="attachment://SUCCESS.png")
        await ctx.send(embed=embed, file=file)

async def setup(bot):
    await bot.add_cog(Expense(bot))