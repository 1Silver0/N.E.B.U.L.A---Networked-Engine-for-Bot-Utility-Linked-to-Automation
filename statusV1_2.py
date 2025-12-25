import discord
from discord.ext import commands
import psutil
import GPUtil
import wmi
import os
import asyncio
from concurrent.futures import ThreadPoolExecutor as TPE
import speedtest

class Status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def get_speed(self):
        loop = asyncio.get_running_loop()
        with TPE() as pool:
            st = await loop.run_in_executor(pool, speedtest.Speedtest)
            await loop.run_in_executor(pool, st.get_best_server)
            down = await loop.run_in_executor(pool, st.download)
            up = await loop.run_in_executor(pool, st.upload)
            ping = round(st.results.ping, 2)
        return round(down / 1_000_000, 2), round(up / 1_000_000, 2), ping

    @commands.command()
    async def status(self, ctx):
        file1 = discord.File("NEBULA/NebulaV1_2/WAIT....png", filename="WAIT....png")
        embed1 = discord.Embed(description="Performing tests...", color=discord.Color.yellow())
        embed1.set_footer(text="N.E.B.U.L.A Operating Systems - Powered by Python")
        embed1.set_image(url="attachment://WAIT....png")
        await ctx.send(embed=embed1, file=file1)

        c = wmi.WMI()
        cpu_name = [cpu.Name for cpu in c.Win32_Processor()][0]
        cpu_cores = psutil.cpu_count(logical=True)
        ram_total = round(psutil.virtual_memory().total / (1024**3), 2)
        ram_used = round(psutil.virtual_memory().used / (1024**3), 2)
        storage_total = round(psutil.disk_usage('/').total / (1024**3), 2)
        gpus = GPUtil.getGPUs()
        gpu_name = gpus[0].name if gpus else "No GPUs found"

        process = psutil.Process(os.getpid())
        cpu_percent = psutil.cpu_percent(interval=1)
        ram_bot = round(process.memory_info().rss / (1024**2), 2)

        down, up, ping = await self.get_speed()

        file2 = discord.File("NEBULA/NebulaV1_2/SUCCESS.png", filename="SUCCESS.png")
        embed2 = discord.Embed(title="N.E.B.U.L.A Test", color=discord.Color.green())
        embed2.add_field(name="System Status", value="✅ Commands\n✅ Network Connection\n✅ Virtual Storage\n✅ Information Sites")
        embed2.add_field(name="CPU Usage", value=f"{cpu_percent} %", inline=False)
        embed2.add_field(name="RAM Usage", value=f"{ram_bot} MB", inline=True)
        embed2.add_field(name="Version", value="V1.2", inline=False)
        embed2.set_image(url="attachment://SUCCESS.png")

        file3 = discord.File("NEBULA/NebulaV1_2/SUCCESS.png", filename="SUCCESS.png")
        embed3 = discord.Embed(title="PC Test", color=discord.Color.green())
        embed3.add_field(name="CPU Model", value=f"{cpu_name}", inline=False)
        embed3.add_field(name="CPU Cores", value=f"{cpu_cores}", inline=True)
        embed3.add_field(name="RAM", value=f"{ram_total} GB", inline=False)
        embed3.add_field(name="Disk Space", value=f"{storage_total} GB", inline=True)
        embed3.add_field(name="GPU", value=f"{gpu_name}", inline=False)
        embed3.set_image(url="attachment://SUCCESS.png")

        file4 = discord.File("NEBULA/NebulaV1_2/SUCCESS.png", filename="SUCCESS.png")
        embed4 = discord.Embed(title="Internet Test", color=discord.Color.green())
        embed4.add_field(name="Download", value=f"{down} Mbps", inline=False)
        embed4.add_field(name="Upload", value=f"{up} Mbps", inline=True)
        embed4.add_field(name="Ping", value=f"{ping} Ms", inline=False)
        embed4.set_footer(text="N.E.B.U.L.A Operating Systems - Powered by Python")
        embed4.set_image(url="attachment://SUCCESS.png")

        await ctx.send(embed=embed2, file=file2)
        await ctx.send(embed=embed3, file=file3)
        await ctx.send(embed=embed4, file=file4)

async def setup(bot):
    await bot.add_cog(Status(bot))
