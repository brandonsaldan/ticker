from discord.ext import commands
import discord
from datetime import datetime as d
import time
import requests

class Ping(commands.Cog):

    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print("Ping Loaded!")

    @commands.command(name='ping')
    async def ping(self, ctx):
        embedping = discord.Embed(title="Ticker Ping", color=discord.Color(0x21CE99))
        embedping.add_field(name="Ping", value=f'{round(self.client.latency * 1000)}ms')
        embedping.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/b/b9/Robinhood_Logo.png")
        embedping.set_footer(text=ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.send(embed=embedping)
        
def setup(client):
    client.add_cog(Ping(client))