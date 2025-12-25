import discord
from discord.ext import commands
from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os

load_dotenv()

key = os.getenv("NEBULA_KEY") # I saved my key in a .env file

if not key:
    key = Fernet.generate_key().decode()
    with open(".env", "a") as f:
        f.write(f"NEBULA_KEY={key}\n")
    print(f"Generated new NEBULA_KEY: {key}")

cipher = Fernet(key.encode())

class Decrypt(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def decrypt(self, ctx, *, text: str):
        try:
            decrypted = cipher.decrypt(text.encode()).decode()

            file1 = discord.File("NEBULA/NebulaV1_2/SUCCESS.png", filename="SUCCESS.png")
            embed1 = discord.Embed(title=f"Decryption of '{text}':", description=f"{decrypted}", color=discord.Color.green())
            embed1.set_footer(text="N.E.B.U.L.A Operating Systems - Powered by Powered by Python")
            embed1.set_image(url="attachment://SUCCESS.png")
            await ctx.send(embed=embed1, file=file1)
        except Exception as e:
            file2 = discord.File("NEBULA/NebulaV1_2/ERROR.png", filename="ERROR.png")
            embed2 = discord.Embed(description=f"Error: {e}", color=discord.Color.red())
            embed2.set_footer(text="N.E.B.U.L.A Operating Systems - Powered by Python")
            embed2.set_image(url="attachment://ERROR.png")
            await ctx.send(embed=embed2, file=file2)

async def setup(bot):
    await bot.add_cog(Decrypt(bot))