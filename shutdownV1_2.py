import discord
from discord.ext import commands
import asyncio

command_steps = [".balance", ".calc", ".clean", ".crypto", ".dailreport", ".decrypt", ".define", ".encrypt", ".eshutdown", ".expense", ".forget", ".income", ".info", ".news", ".nhelp", ".openbox", ".recall", ".remember", ".research", ".setbox", ".setdailyreport", ".shutdown", ".status", ".unitconvert", "**Commands Unloaded**"]
network_steps = ["Channel Unverified", "Secure Channel Closed", "Connection Closed", "DNS Unresolved", "**Network Connection Abolished**"]
storage_steps = ["Access Permissions Aborted", "Virtual Storage Seperated", "File Clusters Indexed", "Data Integrity Verified", "Memory Buffers Retained", "**Storage Unlinked**"]
site_steps = ["Data Streams Unverified", "Sites Discarded", "**Information Sites Unavailable**"]

def build_combined_status(commands, completed_cmds, network_steps=[], completed_net=0, storage_steps=[], completed_storage=0, site_steps=[], completed_site=0):
    lines = []
    # Commands
    for i, cmd in enumerate(commands):
        lines.append(f"⬛ {cmd}" if i < completed_cmds else f"#️⃣ {cmd}")

    # Network
    if network_steps:
        lines.append("")
        for i, step in enumerate(network_steps):
            lines.append(f"⬛ {step}" if i < completed_net else f"🛜 {step}")

    # Storage
    if storage_steps:
        lines.append("")
        for i, step in enumerate(storage_steps):
            lines.append(f"⬛ {step}" if i < completed_storage else f"*️⃣ {step}")

    # Information sites
    if site_steps:
        lines.append("")
        for i, step in enumerate(site_steps):
            lines.append(f"⬛ {step}" if i < completed_site   else f"ℹ️ {step}")

    return "\n".join(lines)

class Shutdown(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def shutdown(self, ctx):
        file1 = discord.File("NEBULA/NebulaV1_2/LOADING....png", filename="LOADING....png")
        embed1 = discord.Embed(title="Systems Unloading...", description=build_combined_status(command_steps, 0), color=discord.Color.blue())
        embed1.set_footer(text="N.E.B.U.L.A Operating Systems - Powered by Python")
        embed1.set_image(url="attachment://LOADING....png")
        message = await ctx.send(embed=embed1, file=file1)
        # Load commands
        for i in range(1, len(command_steps)+1):
            await asyncio.sleep(0.1)
            embed1.description = build_combined_status(command_steps, i)
            embed1.color = discord.Color.blue()
            await message.edit(embed=embed1)

        # Load network steps
        for i in range(1, len(network_steps)+1):
            await asyncio.sleep(0.4)
            embed1.description = build_combined_status(command_steps, len(command_steps), network_steps, i)
            await message.edit(embed=embed1)

        # Load storage steps
        for i in range(1, len(storage_steps)+1):
            await asyncio.sleep(0.4)
            embed1.description = build_combined_status(command_steps, len(command_steps), network_steps, len(network_steps), storage_steps, i)
            await message.edit(embed=embed1)

        # Load information sites steps
        for i in range(1, len(site_steps)+1):
            await asyncio.sleep(0.4)
            embed1.description = build_combined_status(command_steps, len(command_steps), network_steps, len(network_steps), storage_steps, len(storage_steps), site_steps, i)
            await message.edit(embed=embed1)
        
        final_file = discord.File("NEBULA/NebulaV1_2/NEBULAOPERATINGSYSTEMS.png", filename="NEBULAOPERATINGSYSTEMS.png")
        final_embed = discord.Embed(description="N.E.B.U.L.A is **offline** - **Not ready** to assist you", color=discord.Color.purple())
        final_embed.set_footer(text="N.E.B.U.L.A Operating Systems - Powered by Python")
        final_embed.set_image(url="attachment://NEBULAOPERATINGSYSTEMS.png")
        await message.edit(embed=final_embed, attachments=[final_file])

        await self.bot.close()

async def setup(bot):
    await bot.add_cog(Shutdown(bot))