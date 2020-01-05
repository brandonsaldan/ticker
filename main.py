import discord
import asyncio
import requests
import json
import string
import os
import os.path
import traceback
import time

from discord.ext import commands
from discord.ext.commands import Bot
from io import StringIO
from os import listdir
from os.path import isfile, join

bot = commands.Bot(command_prefix="s.")
bot.remove_command("help")
client = discord.Client()

@bot.event
async def on_ready():
    number_of_servers = len(bot.servers)
    await bot.change_presence(game=discord.Game(name="on {} servers".format(number_of_servers)))
    print("Launched...")
    print("My name is " + bot.user.name)
    print("ID: " + bot.user.id)

@bot.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title='StockBot Help', description="**Invite Link:** https://discordapp.com/api/oauth2/authorize?client_id=663214101320695833&permissions=8&scope=bot", color = 0x21CE99)
    embed.add_field(name="Specific Information", value="You can get more specific information on each command by doing `s.[module]info` for example, `s.stockpriceinfo` will give you a complete description of each command in that module.")
    await bot.send_message(ctx.message.channel, embed=embed)
    print("Help command recieved.")
    print("--------------------")

@bot.command(pass_context=True)
async def stockpriceinfo(ctx):
    embed = discord.Embed(title='Command Info', description="Current Stock Price", color = 0x21CE99)
    embed.add_field(name="Information", value="Using s.stockprice will give you the current price of a stock of your choosing.")
    await bot.send_message(ctx.message.channel, embed=embed)
    print("stockpriceinfo command recieved.")
    print("--------------------")

@bot.command(pass_context=True)
async def reload(ctx):
        if ctx.message.author.id == "261953350860275713":
            # Loading
            for extension in [f.replace('.py', "") for f in listdir("cogs") if isfile(join("cogs", f))]:
                try:
                    if not "__init__" in extension:
                        print("Reloading {}...".format(extension))
                        bot.unload_extension("cogs." + extension)
                        loadingCogMessage = await bot.say("Loading {}..".format(extension))
                        bot.load_extension("cogs." + extension)
                        await bot.edit_message(loadingCogMessage, "✅ | {} has been loaded.".format(extension))
                except Exception as e:
                    print("Failed to load cog {}".format(extension))
                    await bot.say("⛔️ | Failed to load cog {}".format(extension))
                    traceback.print_exc()
        else:
            print("Unauthorized user has attempted to reload modules.. Stopped :)")
            await bot.say("⛔️ | Bot owner only!")

async def LoadCogs():
    for extension in [f.replace('.py', "") for f in listdir("cogs") if isfile(join("cogs", f))]:
        try:
            if not "__init__" in extension:
                print("Loading {}...".format(extension))
                bot.load_extension("cogs." + extension)
        except Exception as e:
            print("Failed to load cog {}".format(extension))
            traceback.print_exc()

@bot.command(pass_context=True)
@commands.cooldown(1, 7, commands.BucketType.user)
async def ping(ctx):
    time_then = time.monotonic()
    pinger = await bot.send_message(ctx.message.channel, 'Pong | Loading latency..')
    ping = '%.2f' % (1000*(time.monotonic()-time_then))
    #await bot.edit_message(pinger, 'ℹ️ | **Pong!** ``' + ping + 'ms``') # you can edit this to say whatever you want really. Hope this helps.
    embed = discord.Embed(colour=discord.Colour(0x989898))

    embed.add_field(name="StockBot Ping", value="Ping: **{}ms** ".format(ping))
    await bot.delete_message(pinger)
    await bot.say(embed=embed)
    print("ping command recieved.")
    print("--------------------")

@ping.error
async def ping_error(error, ctx):
    if isinstance(error, discord.ext.commands.errors.CommandOnCooldown):
        msg = await bot.send_message(ctx.message.channel, "{} You're doing that too fast, please slow down.".format(ctx.message.author.mention))
        await asyncio.sleep(6)
        await bot.delete_message(msg)
        print("ping error.")
        print("--------------------")

bot.run("")