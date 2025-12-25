import discord
from discord.ext import commands
import aiohttp
import matplotlib.pyplot as plt
from io import BytesIO
import datetime
import asyncio

recent_messages = set()

timeout = aiohttp.ClientTimeout(total=15)

class Crypto(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(timeout=timeout)

    @commands.command()
    async def crypto(self, ctx, coin: str = "bitcoin", days: int = 7):
        msg_id = ctx.message.id
        if msg_id in recent_messages:
            return
        recent_messages.add(msg_id)

        try:
            coin_id = coin.lower()
            url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart?vs_currency=usd&days={days}"

            data = None
            for attempt in range(3):
                try:
                    async with self.session.get(url) as resp:
                        resp.raise_for_status()
                        data = await resp.json()
                        break
                except (aiohttp.ClientConnectionError, aiohttp.ServerTimeoutError) as e:
                    if attempt < 2:
                        await asyncio.sleep(1)
                    else:
                        file1 = discord.File("NEBULA/NebulaV1.2/ERROR.png", filename="ERROR.png")
                        embed1 = discord.Embed(description=f"Error: **{e}**", color=discord.Color.red())
                        embed1.set_footer(text="N.E.B.U.L.A Operating Systems - Powered by Python")
                        embed1.set_thumbnail(url="attachment://ERROR.png")
                        return await ctx.send(embed=embed1, file=file1)

            if "prices" not in data or not data["prices"]:
                file2 = discord.File("NEBULA/NebulaV1.2/ERROR.png", filename="ERROR.png")
                embed2 = discord.Embed(description=f"Error: **CoinNotFound**", color=discord.Color.red())
                embed2.set_footer(text="N.E.B.U.L.A Operating Systems - Powered by Python")
                embed2.set_thumbnail(url="attachment://ERROR.png")
                return await ctx.send(embed=embed2, file=file2)

            timestamps = [datetime.datetime.fromtimestamp(p[0]/1000).strftime('%d %b') for p in data['prices']]
            prices = [p[1] for p in data['prices']]

            plt.figure(figsize=(12, 8))
            plt.plot(timestamps, prices, marker='o', color='black')
            plt.title(f"{coin.capitalize()} Price Last {days} Days")
            plt.xlabel("Date")
            plt.ylabel("Price (USD)")
            plt.grid(True)
            plt.tight_layout()

            buffer = BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            plt.close()

            file3 = discord.File(fp=buffer, filename=f"{coin_id}_chart.png")
            embed3 = discord.Embed(title=f"{coin.capitalize()} Price Chart", color=discord.Color.green())
            embed3.set_image(url=f"attachment://{coin_id}_chart.png")
            embed3.set_footer(text="N.E.B.U.L.A Operating Systems - Powered by Python")
            embed3.set_thumbnail(url="attachment://SUCCESS.png")
            await ctx.send(embed=embed3, file=file3)

        finally:
            await asyncio.sleep(5)
            recent_messages.remove(msg_id)

async def setup(bot):
    await bot.add_cog(Crypto(bot))