import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='XD')
client = discord.Client()



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@bot.command()
async def help(ctx, help):
    await ctx.send("Hola, todavia no me asignan comandos")

@bot.command()
async def suma(ctx, a: int, b: int):
    await ctx.send(a + b)

    


client.run('NzcwNDM0OTA2NTkyNjQxMDU1.X5dhaw.FoocCI0gbXBx_V0hEQ-4ZfSji84')