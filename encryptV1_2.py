import discord
from discord.ext import commands
from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os

load_dotenv()

key_str = os.getenv("NEBULA_KEY") # Saved my key with a .env file

if not key_str:
    key = Fernet.generate_key()
    with open(".env", "a") as f:
        f.write(f"NEBULA_KEY={key}\n")
    print(f"Generated new NEBULA_KEY: {key.decode()}")
else:
    key = key_str.encode()

cipher = Fernet(key)

class Encrypt(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def encrypt(self, ctx, *, text: str):
        encrypted = cipher.encrypt(text.encode()).decode()

        file1 = discord.File("NEBULA/NebulaV1_2/SUCCESS.png", filename="SUCCESS.png")
        embed1 = discord.Embed(title=f"Encryption of '{text}':", description=f"{encrypted}", color=discord.Color.green())
        embed1.set_footer(text="N.E.B.U.L.A Operating Systems - Powered by Python")
        embed1.set_image(url="attachment://SUCCESS.png")
        await ctx.send(embed=embed1, file=file1)

async def setup(bot):
    await bot.add_cog(Encrypt(bot))