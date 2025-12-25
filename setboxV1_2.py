import discord
from discord.ext import commands
from discord.ui import Modal, TextInput, View, Button
import aiosqlite

# ----------------- Modal -----------------
class BoxModal(Modal, title="Enter Box Information"):
    content = TextInput(
        label="Content",
        placeholder="Enter the content you want in your Box...",
        required=True,
        max_length=100
    )
    password = TextInput(
        label="Password",
        placeholder="Enter the password you want for your Box...",
        required=True,
        max_length=15
    )

    def __init__(self, cog, user_id):
        super().__init__()
        self.cog = cog
        self.user_id = user_id

    async def on_submit(self, interaction: discord.Interaction):
        # Gem til SQLite
        async with aiosqlite.connect("nbsV1.1.db") as db:
            await db.execute("""CREATE TABLE IF NOT EXISTS passwords (id INTEGER PRIMARY KEY, content TEXT, password TEXT)""")
            await db.execute("INSERT OR REPLACE INTO passwords (id, content, password) VALUES (?, ?, ?)", (self.user_id, self.content.value, self.password.value))
            await db.commit()

        # Send embed to user
        file1 = discord.File("NEBULA/NebulaV1_2/SUCCESS.png", filename="SUCCESS.png")
        embed = discord.Embed(
            title="Your Box has been set",
            description=f"Your Box content is now **{self.content.value}**\n"
                        f"Your Box password is now **{self.password.value}**",
            color=discord.Color.green()
        )
        embed.set_footer(text="N.E.B.U.L.A Operating Systems - Powered by Python")
        embed.set_image(url="attachment://SUCCESS.png")
        await interaction.response.send_message(embed=embed, file=file1, ephemeral=True)

# ----------------- Button + View -----------------
class SetBoxButton(View):
    def __init__(self, cog):
        super().__init__(timeout=None)  # No timeout
        self.cog = cog

    @discord.ui.button(label="Set your Box", style=discord.ButtonStyle.green)
    async def set_box(self, button: Button, interaction: discord.Interaction):
        modal = BoxModal(self.cog, interaction.user.id)
        await interaction.response.send_modal(modal)

# ----------------- Cog -----------------
class Setbox(commands.Cog): # BROKEN, W.I.P
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def setbox(self, ctx: commands.Context):
        view = SetBoxButton(self)
        embed = discord.Embed(description="Click the button below to set your Box:", color=discord.Color.green())
        embed.set_footer(text="N.E.B.U.L.A Operating Systems - Powered by Python")
        await ctx.send(embed=embed, view=view)

# ----------------- Setup -----------------
async def setup(bot):
    await bot.add_cog(Setbox(bot))