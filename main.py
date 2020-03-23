import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = "t.")

cogs = ["cogs.ping", "cogs.stockprice"]
client.remove_command("help")

@client.event
async def on_ready():
    print("Launched...")
    print(f"Logged in as {client.user.name} - {client.user.id}")
    for cog in cogs:
        client.load_extension(cog)
    return

@client.command(pass_context=True)
async def help(ctx):
    embedhelp = discord.Embed(title="Ticker Help", color=discord.Color(0x21CE99))
    embedhelp.add_field(name="t.stockprice (stock)", value="Returns the current price of a selected stock.", inline=False)
    embedhelp.add_field(name="t.rate (stock)", value="**(WIP)** Returns analyst recommendations for a selected stock.", inline=False)
    embedhelp.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/b/b9/Robinhood_Logo.png")
    embedhelp.set_footer(text=ctx.author.name, icon_url = ctx.author.avatar_url)
    await ctx.send(embed=embedhelp)

client.run("")