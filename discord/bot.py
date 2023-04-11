import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print("----------------------------------")
    print('Bot Ready!')
    print('Logged in as: {0.user}'.format(bot))
    print("----------------------------------")
    
@bot.command()
async def hello(ctx):
    channel = bot.get_channel(1095463794416816138)
    await channel.send(f'Hello there {ctx.author.mention}!')

bot.run(TOKEN)
