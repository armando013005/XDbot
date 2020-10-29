import discord
from discord.ext import commands
import datetime
import asyncio
client = discord.Client()
bot = commands.Bot(command_prefix='*', description="estoy en construccion :D")

@bot.command()
async def ping(ctx, description= "pong!!"):
    await ctx.send('Pong!!')

@bot.command()
async def suma(ctx,a: int, b: int):
    await ctx.send(a + b)

@bot.event
async def on_ready():
    game= discord.Game("*help | Agregame a tu sv fav :D")
    await bot.change_presence(status=discord.Status.online, activity=game)
    print("ya")


@bot.command()
async def info(ctx):
    await ctx.send(embed = discord.Embed(
     title=f"{ctx.guild.name}",
     description="Info of the this server", 
     timestamp=datetime.datetime.utcnow(), 
     color=discord.Color.blue(),
     nameOwner = "Server Owner",ValueOwner=f"{ctx.guild.owner}",
     nameRegion="Server Region", ValueRegion =f"{ctx.guild.region}",
     nameServerID="Server ID", ValueServerID=f"{ctx.guild.id}")
    )
     

bot.run('NzcwNDM0OTA2NTkyNjQxMDU1.X5dhaw.FoocCI0gbXBx_V0hEQ-4ZfSji84')