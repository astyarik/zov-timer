import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()
token = os.getenv("ZOV")

intents = discord.Intents.default()
intents.message_content = True

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=".", intents=intents)

    async def setup_hook(self):
        await self.tree.sync()
        print("Slash-команды синхронизированы")

bot = MyBot()

# Slash-команда
@bot.tree.command(name="zov", description="Таймер")
@app_commands.describe(seconds="Длина работы (не более 100с)")
async def slash_zov(interaction: discord.Interaction, seconds: int = 60):
    if seconds > 100:
        seconds = 100
    
    await interaction.response.send_message("ZOV Таймер\nZOV\n(Это 1 секунда)")
    message = await interaction.original_response()

    for x in range(2, seconds + 1):
        await asyncio.sleep(1)
        await message.edit(content=f'ZOV Таймер\n{"ZOV " * x}\n(Это {x} секунд)')

# Обычная (.zov)
@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def zov(ctx, seconds: int = 60):
    if seconds > 100:
        seconds = 100

    message = await ctx.send("ZOV")
    for x in range(2, seconds + 1):
        await asyncio.sleep(1)
        await message.edit(content=f'ZOV Таймер\n{"ZOV " * x}\n(Это {x} секунд)')

@bot.event
async def on_ready():
    print(f"{bot.user} работает")

bot.run(token)
