import discord
from discord.ext import commands
import json
import os

MEMORY = "YOUR_STORAGE_FILE"

def load_data():
    try:
        with open(MEMORY, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: File was not found, returning empty dict.")
        return {}
    except json.JSONDecodeError:
        print("Error: JSON is corrupted, returning empty dict.")
        return {}
    except Exception as e:
        print(f"Error: Unexpected error: {e}, returning empty dict.")
        return {}
    
def save_data(data):
    if not os.path.exists(MEMORY):
       with open(MEMORY, "w") as f:
           f.write("{}") 
    try:
        with open(MEMORY, "w") as f:
            return json.dump(data, f, indent=4)
    except PermissionError:
        return print(f"Error: Cannot write to {MEMORY}, permission was denied.")
    except Exception as e:
        return print(f"Error: Unexpected error: {e}.")

class Setdailyreport(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def setdailyreport(self, ctx, coin: str = "bitcoin"):
        try:
            data = load_data()
        except Exception as e:
            file1 = discord.File("NEBULA/NebulaV1_2/ERROR.png", filename="ERROR.png")
            embed1 = discord.Embed(description=f"Error: **{e}**", color=discord.Color.red())
            embed1.set_footer(text="N.E.B.U.L.A Operating Systems - Powered by Python")
            embed1.set_thumbnail(url="attachment://ERROR.png")
            await ctx.send(embed=embed1, file=file1)

        user_id = str(ctx.author.id)
        data[user_id] = coin.lower()
        save_data(data)

        file2 = discord.File("NEBULA/NebulaV1_2/SUCCESS.png")
        embed2 = discord.Embed(description=f"Coin is set as **{coin}**", color=discord.Color.green())
        embed2.set_footer(text="N.E.B.U.L.A Operating Systems - Powered by Python")
        embed2.set_image(url="attachment://SUCCESS.png")
        await ctx.send(embed=embed2, file=file2)

async def setup(bot):
    await bot.add_cog(Setdailyreport(bot))