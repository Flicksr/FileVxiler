import discord

from discord.ext import commands

import os

intents = discord.Intents.default()

intents.message_content = True

client = commands.Bot(command_prefix='Bot prefix Here', intents=intents)







    

@client.command()

async def uploadFile(ctx):

    if ctx.message.attachments:

        for file in ctx.message.attachments:

            await file.save(f'assets/saves/{file.filename}')
       
    await ctx.send('File Successfully Uploaded To assets/saves If got any issue just type /Support',)


@client.command()

async def FilesOfDb(ctx):

    files = '\n'.join([file for file in os.listdir('assets/saves')])

    await ctx.send(f'List of Full uploaded files:\n{files}')

@client.command()

async def GetFile(ctx, file_name):

    try:

        await ctx.send(file=discord.File(f'assets/saves/{file_name}'))
        await ctx.send('Done File Successfully Been Sent If Any issues Just Type /Support')

    except FileNotFoundError:

        await ctx.send('File not found Code 1002.')    

@client.command()

async def Support(ctx):

       await ctx.send('Message Here')




        


    

client.run('Your token here')
