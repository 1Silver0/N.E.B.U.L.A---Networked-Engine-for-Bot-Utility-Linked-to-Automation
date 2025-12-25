import discord
from discord.ext import commands
from discord.ui import View, Select, Modal, TextInput

# ----------------- Dictionaries -----------------
LENGTH = {
    "m": 1, "km": 1000, "cm": 0.01, "mm": 0.001,
    "mi": 1609.34, "yd": 0.9144, "ft": 0.3048, "in": 0.0254
}

WEIGHT = {
    "kg": 1, "g": 0.001, "mg": 0.000001, "lb": 0.453592, "oz": 0.0283495
}

TEMPERATURE = ["C", "F", "K"]

SPEED = {
    "m/s": 1, "km/h": 1000/3600, "mph": 1609.34/3600, "ft/s": 0.3048
}

ENERGY = {
    "j": 1, "kj": 1000, "cal": 4.184, "kcal": 4184, "wh": 3600, "kwh": 3600000
}

PRESSURE = {
    "Pa": 1, "kPa": 1000, "bar": 100000, "atm": 101325, "psi": 6894.76
}

# ----------------- Views & Modals -----------------
class CategorySelect(Select):
    def __init__(self):
        options = [discord.SelectOption(label=cat) for cat in ["Length", "Weight", "Temperature", "Speed", "Energy", "Pressure"]]
        super().__init__(placeholder="Choose category", options=options, min_values=1, max_values=1)

    async def callback(self, interaction):
        category = self.values[0]
        await interaction.response.send_message(
            f"Category chosen: {category}. Choose from_unit.", 
            view=FromUnitView(category)
        )

class CategoryView(View):
    def __init__(self):
        super().__init__()
        self.add_item(CategorySelect())

class FromUnitSelect(Select):
    def __init__(self, category):
        self.category = category
        units_dict = {
            "Length": LENGTH,
            "Weight": WEIGHT,
            "Speed": SPEED,
            "Energy": ENERGY,
            "Pressure": PRESSURE,
            "Temperature": {u: u for u in TEMPERATURE}
        }
        options = [discord.SelectOption(label=u) for u in units_dict[category].keys()]
        super().__init__(placeholder="Choose from_unit", options=options, min_values=1, max_values=1)

    async def callback(self, interaction):
        from_unit = self.values[0]
        await interaction.response.send_message(
            f"From_unit chosen: {from_unit}. Choose to_unit.", 
            view=ToUnitView(self.category, from_unit)
        )

class FromUnitView(View):
    def __init__(self, category):
        super().__init__()
        self.add_item(FromUnitSelect(category))

class ToUnitSelect(Select):
    def __init__(self, category, from_unit):
        self.category = category
        self.from_unit = from_unit
        units_dict = {
            "Length": LENGTH,
            "Weight": WEIGHT,
            "Speed": SPEED,
            "Energy": ENERGY,
            "Pressure": PRESSURE,
            "Temperature": {u: u for u in TEMPERATURE}
        }
        options = [discord.SelectOption(label=u) for u in units_dict[category].keys() if u != from_unit]
        super().__init__(placeholder="Choose to_unit", options=options, min_values=1, max_values=1)

    async def callback(self, interaction):
        to_unit = self.values[0]
        cog = interaction.client.get_cog("Unitconvert")
        await interaction.response.send_modal(AmountModal(self.category, self.from_unit, to_unit, cog))

class ToUnitView(View):
    def __init__(self, category, from_unit):
        super().__init__()
        self.add_item(ToUnitSelect(category, from_unit))

class AmountModal(Modal, title="Enter amount"):
    amount = TextInput(label="Amount", placeholder="Enter a number here...")

    def __init__(self, category, from_unit, to_unit, cog):
        super().__init__()
        self.category = category
        self.from_unit = from_unit
        self.to_unit = to_unit
        self.cog = cog

    async def on_submit(self, interaction):
        try:
            value = float(self.amount.value)
            result = await self.cog.unitconvert_logic(self.category, value, self.from_unit, self.to_unit)
            await interaction.response.send_message(f"{value} {self.from_unit} = {result} {self.to_unit}")
        except Exception as e:
            await interaction.response.send_message(f"Error: {e}")

class Unitconvert(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def unitconvert(self, ctx):
        embed1 = discord.Embed(description="Choose a category for conversion:", color=discord.Color.purple())
        embed1.set_footer(text="N.E.B.U.L.A Operating Systems - Powered by Python")
        await ctx.send(embed=embed1, view=CategoryView())

    # Logic separated for dropdown/modal usage
    async def unitconvert_logic(self, category, amount, from_unit, to_unit):
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        if category == "Temperature" or (from_unit.upper() in TEMPERATURE and to_unit.upper() in TEMPERATURE):
            return self.convert_temperature(amount, from_unit.upper(), to_unit.upper())
        elif category == "Length" or (from_unit in LENGTH and to_unit in LENGTH):
            return amount * LENGTH[from_unit] / LENGTH[to_unit]
        elif category == "Weight" or (from_unit in WEIGHT and to_unit in WEIGHT):
            return amount * WEIGHT[from_unit] / WEIGHT[to_unit]
        elif category == "Speed" or (from_unit in SPEED and to_unit in SPEED):
            return amount * SPEED[from_unit] / SPEED[to_unit]
        elif category == "Energy" or (from_unit in ENERGY and to_unit in ENERGY):
            return amount * ENERGY[from_unit] / ENERGY[to_unit]
        elif category == "Pressure" or (from_unit in PRESSURE and to_unit in PRESSURE):
            return amount * PRESSURE[from_unit] / PRESSURE[to_unit]
        else:
            raise ValueError("Invalid unit or category")

    def convert_temperature(self, amount, from_unit, to_unit):
        if from_unit == "C":
            if to_unit == "F":
                return round((amount * 9/5) + 32, 6)
            elif to_unit == "K":
                return round(amount + 273.15, 6)
        elif from_unit == "F":
            if to_unit == "C":
                return round((amount - 32) * 5/9, 6)
            elif to_unit == "K":
                return round((amount - 32) * 5/9 + 273.15, 6)
        elif from_unit == "K":
            if to_unit == "C":
                return round(amount - 273.15, 6)
            elif to_unit == "F":
                return round((amount - 273.15) * 9/5 + 32, 6)
        return amount

async def setup(bot):
    await bot.add_cog(Unitconvert(bot))