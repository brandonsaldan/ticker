import discord
import asyncio
import requests
import json
import string
import os
import os.path
import traceback

from discord.ext import commands
from discord.ext.commands import Bot
from io import StringIO
from os import listdir
from os.path import isfile, join

class StockPrice(object):
	def __init__(self, bot):
		self.bot = bot
	@commands.command(pass_context=True)
	async def stockprice(self, ctx, *, arg):
		print("stockprice command recieved.")
		print("--------------------")
		embed = discord.Embed(title=arg, color = 0x21CE99)
		embed.set_footer(text="{} | Financial Modeling Prep API ".format(arg), icon_url="https://upload.wikimedia.org/wikipedia/commons/b/b9/Robinhood_Logo.png")
		
		symbol = requests.get("https://financialmodelingprep.com/api/v3/stock/real-time-price/{}".format(arg)).json()
		price = requests.get("https://financialmodelingprep.com/api/v3/stock/real-time-price/{}".format(arg)).json()
		
		embed.add_field(name="Symbol", value="{}".format(symbol.get("symbol", "Not found")))
		embed.add_field(name="Price", value="${}".format(price.get("price", "Not found")))
		await self.bot.say(embed=embed)

def setup(bot):
	bot.add_cog(StockPrice(bot))