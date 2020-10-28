import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('XDhelp'):
        await message.channel.send('Hello!')

client.run('NzcwNDM0OTA2NTkyNjQxMDU1.X5dhaw.wrBkgqGhkWjJZUSB-TfJIs0Ccs4')