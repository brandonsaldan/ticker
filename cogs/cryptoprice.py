import discord
import asyncio
import math
import datetime
import requests
import json
import string
import time
import os
import os.path
import traceback

from discord.ext import commands
from discord.ext.commands import Bot
from datetime import datetime, date
from random import randint
from io import StringIO
from os import listdir
from os.path import isfile, join

class CryptoPrice(object):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(pass_context=True)
    async def cryptoprice(self, ctx, *, arg):
        print("cryptoprice command recieved.")
        print("--------------------")
        embed = discord.Embed(title=arg, color = 0x065FBD)
        embed.set_footer(text="{} | Financial Modeling Prep API ".format(arg), icon_url="https://is2-ssl.mzstatic.com/image/thumb/Purple124/v4/80/fd/3c/80fd3c3a-08e9-c5d9-cfb0-bda3d821209c/AppIcon-0-1x_U007emarketing-0-0-GLES2_U002c0-512MB-sRGB-0-0-0-85-220-0-0-0-5.png/1024x1024bb.jpg")

        symbol = requests.get("https://financialmodelingprep.com/api/v3/cryptocurrency/{}".format(arg)).json()
        price = requests.get("https://financialmodelingprep.com/api/v3/cryptocurrency/{}".format(arg)).json()

        embed.add_field(name="Ticker", value="{}".format(symbol.get("ticker", "Not found")))
        embed.add_field(name="Name", value="{}".format(price.get("name", "Not found")))
        embed.add_field(name="Price", value="${}".format(price.get("price", "Not found")))
        await self.bot.say(embed=embed)

def setup(bot):
	bot.add_cog(CryptoPrice(bot))