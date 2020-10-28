import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='*')
client = discord.Client()
class MyClient(discord.client):
    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))

    @client.event
    async def on_message(self, message):
        if message.content.startswith("*Hello" or "*hola"):
            await message.channel.send("Hi" or "hola")

client.run('NzcwNDM0OTA2NTkyNjQxMDU1.X5dhaw.FoocCI0gbXBx_V0hEQ-4ZfSji84')