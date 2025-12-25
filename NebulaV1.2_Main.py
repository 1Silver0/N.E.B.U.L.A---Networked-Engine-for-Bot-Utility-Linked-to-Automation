import discord
from discord.ext import commands
import asyncio
import os

TOKEN = "BOT_TOKEN_HERE"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)

async def load_all_extensions():
    commands_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "commands")
    
    for filename in os.listdir(commands_path):
        if filename.endswith(".py") and filename != "__init__.py":
            extension_name = f"commands.{filename[:-3]}"
            try:
                await bot.load_extension(extension_name)
                print(f"Loaded {extension_name}✅")
            except Exception as e:
                print(f"Failed to load {extension_name}❌: {e}")

command_steps = [".balance", ".calc", ".clean", ".crypto", ".dailreport", ".decrypt", ".define", ".encrypt", ".eshutdown", ".expense", ".forget", ".income", ".info", ".news", ".nhelp", ".openbox", ".recall", ".remember", ".research", ".setbox", ".setdailyreport", ".shutdown", ".status", ".unitconvert", "**Commands Loaded**"]
network_steps = ["DNS Resolved", "Connection Opened", "Secure Channel Established", "Channel Verified", "**Network Connection Established**"]
storage_steps = ["Memory Buffers Allocated", "Data Integrity Verified", "File Clusters Indexed", "Virtual Storage Syncronized", "Access Permissions Finalized", "**Storage Linked**"]
site_steps = ["Sites Scanned", "Data Streams Verified", "Latest Updates Catched", "Latest Updates Syncronized", "**Information Sites Ready**"]

def build_combined_status(commands, completed_cmds, network_steps=[], completed_net=0, storage_steps=[], completed_storage=0, site_steps=[], completed_site=0):
    lines = []
    # Commands
    for i, cmd in enumerate(commands):
        lines.append(f"#️⃣ {cmd}" if i < completed_cmds else f"⬛ {cmd}")

    # Network
    if network_steps:
        lines.append("")
        for i, step in enumerate(network_steps):
            lines.append(f"🛜 {step}" if i < completed_net else f"⬛ {step}")

    # Storage
    if storage_steps:
        lines.append("")
        for i, step in enumerate(storage_steps):
            lines.append(f"*️⃣ {step}" if i < completed_storage else f"⬛ {step}")

    # Information sites
    if site_steps:
        lines.append("")
        for i, step in enumerate(site_steps):
            lines.append(f"ℹ️ {step}" if i < completed_site   else f"⬛ {step}")

    return "\n".join(lines)

@bot.event
async def on_ready():
    print(f"N.E.B.U.L.A online as {bot.user}")
    
    for cog_name, cog in bot.cogs.items():
        print(f"Cog: {cog_name}, Command: {[cmd.name for cmd in cog.get_commands()]}")

    channel = bot.get_channel(1416138983469093049)
    commands_list = sorted(cmd.name for cmd in bot.commands)
    if channel:
        file1 = discord.File("NEBULA/NebulaV1_2/LOADING....png", filename="LOADING....png")
        embed1 = discord.Embed(title="Systems Loading...", description=build_combined_status(commands_list, 0), color=discord.Color.blue())
        embed1.set_footer(text="N.E.B.U.L.A Operating Systems - Powered by Python")
        embed1.set_image(url="attachment://LOADING....png")
        message = await channel.send(embed=embed1, file=file1)

        # Load commands
        for i in range(1, len(commands_list)+1):
            await asyncio.sleep(0.01)
            embed1.description = build_combined_status(command_steps, i)
            embed1.color = discord.Color.blue()
            await message.edit(embed=embed1)

        # Load network steps
        for i in range(1, len(network_steps)+1):
            await asyncio.sleep(0.05)
            embed1.description = build_combined_status(command_steps, len(command_steps), network_steps, i)
            await message.edit(embed=embed1)

        # Load storage steps
        for i in range(1, len(storage_steps)+1):
            await asyncio.sleep(0.05)
            embed1.description = build_combined_status(command_steps, len(command_steps), network_steps, len(network_steps), storage_steps, i)
            await message.edit(embed=embed1)

        # Load information sites steps
        for i in range(1, len(site_steps)+1):
            await asyncio.sleep(0.05)
            embed1.description = build_combined_status(command_steps, len(command_steps), network_steps, len(network_steps), storage_steps, len(storage_steps), site_steps, i)
            await message.edit(embed=embed1)

        final_file = discord.File("NEBULA/NebulaV1_2/NEBULAOPERATINGSYSTEMS.png", filename="NEBULAOPERATINGSYSTEMS.png")
        final_embed = discord.Embed(description="N.E.B.U.L.A is **online** - **Ready** to assist you", color=discord.Color.purple())
        final_embed.set_footer(text="N.E.B.U.L.A Operating Systems - Powered by Python")
        final_embed.set_image(url="attachment://NEBULAOPERATINGSYSTEMS.png")
        await message.edit(embed=final_embed, attachments=[final_file])
    else:
        print("System channel not found, messages will not be sent to Discord.")

async def main():
    async with bot:
        await load_all_extensions()
        await bot.start(TOKEN)

asyncio.run(main())