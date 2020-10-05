####                          ####
#### a simple discord bot that sends you messages back ####
#### written in python        ####
#### code by Squeezy aka endi ####
####                          ####

import discord

myToken = 'Enter your token'

print("program is running. . .")

class MyClient(discord.Client):
    async def on_ready(self):
        print("Ich bin eingeloggt beep beep bop")
    

    async def on_message(self, message):
        if message.author == client.user:
            return
        
        elif message.content.startswith("hello bot") or message.content.startswith('hallo bot'):
            await message.channel.send('Hello.')

        elif message.content == "-help" or message.content == "help me":
            await message.channel.send("usage: " + "\n" + "-help for help" + "\n" + "-news for news")
        
        elif message.content == "-news":
            await message.channel.send("https://blick.ch")

    async def on_member_update(self, before, after):
        roles = discord.utils.get(after.guild.roles, name='random')
        await after.add_roles(roles)


client = MyClient()
client.run(myToken)