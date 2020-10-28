import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='XD')
client = discord.Client()



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@bot.command()
async def ayuda(ctx, ayuda):
    await ctx.send("Hola, todavia no me asignan comandos")

@bot.command()
async def suma(ctx, a: int, b: int):
    await ctx.send(a + b)
    
import typing

@bot.command()
async def ban(ctx, members: commands.Greedy[discord.Member],
                   delete_days: typing.Optional[int] = 0, *,
                   reason: str):
    """Mass bans members with an optional delete_days parameter"""
    for member in members:
        await member.ban(delete_message_days=delete_days, reason=reason)

client.run('NzcwNDM0OTA2NTkyNjQxMDU1.X5dhaw.FoocCI0gbXBx_V0hEQ-4ZfSji84')