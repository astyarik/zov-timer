import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

# Для слеш-команд
class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=".", intents=intents)

    async def setup_hook(self):
        await self.tree.sync()
        print("Slash-команды синхронизированы")

bot = MyBot()

# Слеш-команда
@bot.tree.command(name="zov", description="Таймер ZOV")
async def slash_zov(interaction: discord.Interaction):
    await interaction.response.send_message("ZOV Таймер, он считает до 1 минуты\nZOV\n(Это 1 секунда)")
    message = await interaction.original_response()

    for x in range(2, 61):
        await asyncio.sleep(1)
        await message.edit(content="ZOV Таймер, он считает до 1 минуты\n" + ("ZOV " * x) + f"\n(Это {x} секунд)")

# Обычная команда (.zov)
@bot.command()
async def zov(ctx):
    message = await ctx.send("ZOV")

    for x in range(2, 61):
        await asyncio.sleep(1)
        await message.edit(content="ZOV " * x)

@bot.event
async def on_ready():
    print(f"{bot.user} работает")

bot.run(token)
