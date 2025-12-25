import discord
from discord.ext import commands
import sqlite3
import aiosqlite

MEMORY = "YOUR_STORAGE_FILE"

class Remember(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def remember(self, ctx, key, *, content):
        async with aiosqlite.connect(MEMORY) as db:
            await db.execute("CREATE TABLE IF NOT EXISTS memory (id INTEGER PRIMARY KEY AUTOINCREMENT, user TEXT, key TEXT, content TEXT, UNIQUE(user, key))")
            await db.execute("INSERT OR REPLACE INTO memory (user, key, content) VALUES (?, ?, ?)", (str(ctx.author.id), key, content))
            await db.commit()

        file = discord.File("NEBULA/NebulaV1_2/SUCCESS.png", filename="SUCCESS.png")
        embed = discord.Embed(description=f"**{key}: {content}** is saved", color=discord.Color.green())
        embed.set_footer(text="N.E.B.U.L.A Operating Systems - Powered by Python")
        embed.set_image(url="attachment://SUCCESS.png")
        await ctx.send(embed=embed, file=file)

async def setup(bot):
    await bot.add_cog(Remember(bot))