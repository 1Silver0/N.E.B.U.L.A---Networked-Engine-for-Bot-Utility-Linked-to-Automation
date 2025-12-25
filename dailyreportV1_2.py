import discord
from discord.ext import commands
from datetime import datetime
import json
import pytz
import aiohttp
import os

COIN_MEMORY = "YOUR_STORAGE_FILE"
OPENWEATHER_API_KEY = "YOUR_API_KEY"
CITY = "YOUR_CITY"

def load_coin_memory():
    if not os.path.exists(COIN_MEMORY):
        return {}
    try:
        with open(COIN_MEMORY, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

async def get_coin_price(session, coin_id: str):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": coin_id, "vs_currencies": "usd"}

    async with session.get(url, params=params) as resp:
        data = await resp.json()

    return data[coin_id]["usd"]


async def get_weather(session, city: str, api_key: str):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    async with session.get(url, params=params) as resp:
        data = await resp.json()

    if data.get("cod") != 200:
        return None

    weather = data["weather"][0]["description"].capitalize()
    temp = round(data["main"]["temp"])
    feels_like = round(data["main"]["feels_like"])

    return f"{weather}, {temp}°C (feels like {feels_like}°C)"

class Dailyreport(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dailyreport(self, ctx):
        memory = load_coin_memory()
        user_id = str(ctx.author.id)
        coin_id = memory.get(user_id)

        if coin_id is None:
            file1 = discord.File("NEBULA/NebulaV1_2/ERROR.png", filename="ERROR.png")
            embed1 = discord.Embed(description=f"Error: **CoinDoesNotExist**", color=discord.Color.red())
            embed1.set_footer(text="N.E.B.U.L.A Operating Systems - Powered by Python")
            embed1.set_thumbnail(url="attachment://ERROR.png")
            await ctx.send(embed=embed1, file=file1)

        timeout = aiohttp.ClientTimeout(total=10)

        async with aiohttp.ClientSession(timeout=timeout) as session:
            try:
                price_usd = await get_coin_price(session, coin_id)
            except Exception as e:
                file2 = discord.File("NEBULA/NebulaV1_2/ERROR.png", filename="ERROR.png")
                embed2 = discord.Embed(description=f"Error: **{e}**", color=discord.Color.red())
                embed2.set_footer(text="N.E.B.U.L.A Operating Systems — Powered by Python")
                embed2.set_thumbnail(url="attachment://ERROR.png")
                await ctx.send(embed=embed2, file=file2)

            weather_text = await get_weather(session, city=CITY, api_key=OPENWEATHER_API_KEY)

        if weather_text is None:
            weather_text = "No weather data available"

        danish_tz = pytz.timezone("Europe/Copenhagen")
        now = datetime.now(danish_tz)

        hour = now.hour
        if 5 <= hour < 12:
            greeting = "Good morning"
        elif 12 <= hour < 18:
            greeting = "Good afternoon"
        elif 18 <= hour < 21:
            greeting = "Good evening"
        else:
            greeting = "Good night"
        
        file3 = discord.File("NEBULA/NebulaV1_2/SUCCESS.png", filename="SUCCESS.png")
        embed3 = discord.Embed(title=greeting, color=discord.Color.green())
        embed3.add_field(name="Date & Time", value=now.strftime("%d/%m/%y — %H:%M:%S"), inline=False)
        embed3.add_field(name="Weather", value=weather_text, inline=False)
        embed3.add_field(name=f"{coin_id.upper()} Price", value=f"{price_usd} USD", inline=False)
        embed3.set_footer(text="N.E.B.U.L.A Operating Systems — Powered by Python")
        embed3.set_image(url="attachment://SUCCESS.png")
        await ctx.send(embed=embed3, file=file3)


async def setup(bot):
    await bot.add_cog(Dailyreport(bot))