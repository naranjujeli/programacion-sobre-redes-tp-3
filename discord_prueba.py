import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.lower() == 'hola':
        await message.channel.send(f'Hola, {message.author.mention}!')

bot.run('MTE0MTg4MzI3NDI4MTYxNTUxMA.GNkDP-.EDmhwJZCIU5lTGvnjwYgXkUkmor-c6hEEABbaM')