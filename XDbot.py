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




 @client.event
 asinc def UpdatePresence():

    DiscordRichPresence discordPresence:
    memset(&discordPresence, 0, sizeof(discordPresence)):
    discordPresence.state = "Pon XDhelp para saber mas comandos"
    discordPresence.partyId = "ae488379-351d-4a4f-ad32-2b9b01c91657"
    discordPresence.joinSecret = "MTI4NzM0OjFpMmhuZToxMjMxMjM= "
    Discord_UpdatePresence(&discordPresence)       

client.run('NzcwNDM0OTA2NTkyNjQxMDU1.X5dhaw.n_q183owVdRSF-hzpdoqMNWGW2Q')