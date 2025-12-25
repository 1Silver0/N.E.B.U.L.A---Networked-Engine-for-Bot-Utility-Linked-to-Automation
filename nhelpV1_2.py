import discord
from discord.ext import commands

class Nhelp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def nhelp(self, ctx):
        file = discord.File("NEBULA/NebulaV1_2/NEBULAOPERATINGSYSTEMS.png", filename="NEBULAOPERATINGSYSTEMS.png")
        embed = discord.Embed(title="Help", color=discord.Color.purple())
        embed.add_field(name="Show Balance", value=".balance", inline=False)
        embed.add_field(name="Calculator", value=".calc <calculation>", inline=False)
        embed.add_field(name="Clean", value=".clean <channel> <amount>", inline=False)
        embed.add_field(name="Show Crypto Chart", value=".crypto <coin> <days>", inline=False)
        embed.add_field(name="Show Daily Report", value=".dailyreport", inline=False)
        embed.add_field(name="Decrypt Text", value=".decrypt <text>", inline=False)
        embed.add_field(name="Define A Word", value=".define <word>", inline=False)
        embed.add_field(name="Encrypt Text", value=".encrypt <text>", inline=False)
        embed.add_field(name="Perform An Emergency Shutdown", value=".eshutdown", inline=False)
        embed.add_field(name="Log An Expense", value=".expense <category> <price>", inline=False)
        embed.add_field(name="Forget A Note", value=".forget <keyword>", inline=False)
        embed.add_field(name="Log An Income", value=".income <category> <price>", inline=False)
        embed.add_field(name="N.E.B.U.L.A Information", value=".info", inline=False)
        embed.add_field(name="Get News", value=".news <country> <category>", inline=False)
        embed.add_field(name="N.E.B.U.L.A Help", value=".nhelp", inline=False)
        embed.add_field(name="Open Your Box (BROKEN, W.I.P)", value=".openbox <password>", inline=False)
        embed.add_field(name="Recall A Note", value=".recall <keyword>", inline=False)
        embed.add_field(name="Remember A Note", value=".remember <keyword> <content>", inline=False)
        embed.add_field(name="Do Research", value=".research <query>", inline=False)
        embed.add_field(name="Set/Edit Your Box (BROKEN, W.I.P)", value=".setbox <content> <password>", inline=False)
        embed.add_field(name="Set The Coin For Your Daily Report", value=".setdailyreport <coin>", inline=False)
        embed.add_field(name="Perform A Normal Shutdown", value=".shutdown", inline=False)
        embed.add_field(name="Get A N.E.B.U.L.A Status Report", value=".status", inline=False)
        embed.add_field(name="Do Unit Conversion", value=".unitconvert <amount> <from_unit> <to_unit>", inline=False)
        embed.set_footer(text="N.E.B.U.L.A Operating Systems - Powered by Python")
        embed.set_image(url="attachment://NEBULAOPERATINGSYSTEMS.png")
        await ctx.send(embed=embed, file=file)

async def setup(bot):
    await bot.add_cog(Nhelp(bot))