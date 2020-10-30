import discord
from discord.ext import commands
import datetime
import discord.activity

client = discord.Client()
bot = commands.Bot(command_prefix='XD', description="estoy en construccion :D")
@bot.event
async def on_ready():
    game= discord.Game("XDHelp | Agregame a tu sv fav :D |")
    await bot.change_presence(status=discord.Status.online, activity=game)
    print("ya")

@bot.command()
async def Help(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Info del comando ayuda :D", timestamp=datetime.datetime.utcnow(), color=discord.Color.gold())
    embed.add_field(name="XDHelp", value="Da este comando")
    embed.add_field(name="XDpong", value="Dice ping¡¡")
    embed.add_field(name="XDjoin", value="Dice cuando se unio el usuario")
    embed.add_field(name="XDsuma", value="Es una calculadora de suma xd")
    embed.add_field(name="XDinfo", value="Da la informacion del servidor actual")
    embed.add_field(name="XDQueHace", value="Da la actividad del usuario (en construccion)")
    await ctx.send(embed=embed)
    pass




@bot.command()
async def QueHace(ctx, *, member: discord.Member, BaseActivity: discord.Activity):
    await ctx.send('{0.mention} esta jugando {0.BaseActivity}'.format(member))

@bot.command()
async def join(ctx, *, autor: discord.Member):
    await ctx.send('{0.mention} se unio el {0.joined_at} al servidor 'f"{ctx.guild.name}".format(autor))

@bot.command()
async def ping(ctx, description= "pong!!"):
    await ctx.send('Pong!!')

@bot.command()
async def suma(ctx,a: int, b: int):
    await ctx.send(a + b)

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Informacion del servidor actual :D", timestamp=datetime.datetime.utcnow(), color=discord.Color.gold())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    await ctx.send(embed=embed)

bot.run('NzcwNDM0OTA2NTkyNjQxMDU1.X5dhaw.FoocCI0gbXBx_V0hEQ-4ZfSji84')