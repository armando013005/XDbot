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
        await message.channel.send('Hola, estoy en construccion -XD')




 

client.run('NzcwNDM0OTA2NTkyNjQxMDU1.X5dhaw.n_q183owVdRSF-hzpdoqMNWGW2Q')