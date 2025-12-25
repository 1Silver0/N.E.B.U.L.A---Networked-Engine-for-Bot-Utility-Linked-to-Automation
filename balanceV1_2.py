import discord
from discord.ext import commands
import aiosqlite

class Balance(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def balance(self, ctx):
        user_id = str(ctx.author.id)
        async with aiosqlite.connect("YOUR_STORAGE_FILE") as db:
            async with db.execute("SELECT SUM(price) FROM memory WHERE user = ? AND type = 'income'", (user_id,)) as cursor:
                incomerow = await cursor.fetchone()
                total_income = incomerow[0] if incomerow else 0
            async with db.execute("SELECT SUM(price) FROM memory WHERE user = ? AND type = 'expense'", (user_id,)) as cursor:
                expensesrow = await cursor.fetchone()
                total_expenses = expensesrow[0] if expensesrow else 0

        balance = total_income - total_expenses

        file = discord.File("NEBULA/NebulaV1_2/SUCCESS.png", filename="SUCCESS.png")
        embed = discord.Embed(title="Balance:", color=discord.Color.green())
        embed.add_field(name="Income", value=f"{total_income}", inline=False)
        embed.add_field(name="Expenses", value=f"{total_expenses}", inline=False)
        embed.add_field(name="Balance", value=f"{balance}", inline=False)
        embed.set_footer(text="N.E.B.U.L.A Operating Systems - Powered by Python")
        embed.set_image(url="attachment://SUCCESS.png")

        await ctx.send(embed=embed, file=file)

async def setup(bot):
    await bot.add_cog(Balance(bot))