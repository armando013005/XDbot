import discord
from discord.ext import commands
import datetime
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
async def informacion(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Info of the this server", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")

bot.run('NzcwNDM0OTA2NTkyNjQxMDU1.X5dhaw.FoocCI0gbXBx_V0hEQ-4ZfSji84')