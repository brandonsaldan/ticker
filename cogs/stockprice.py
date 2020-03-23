from discord.ext import commands
import discord
import requests

class StockPrice(commands.Cog):

    def init(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print("StockPrice Loaded!")

    @commands.command(pass_context=True)
    async def stockprice(self, ctx, *, arg):

        symbol = requests.get("https://financialmodelingprep.com/api/v3/stock/real-time-price/{}".format(arg)).json()
        price = requests.get("https://financialmodelingprep.com/api/v3/stock/real-time-price/{}".format(arg)).json()

        embedstockprice = discord.Embed(title="Stock Price", color=discord.Color(0x21CE99))
        embedstockprice.add_field(name="Symbol", value="{}".format(symbol.get("symbol", "Not found")))
        embedstockprice.add_field(name="Price", value ="${}".format(price.get("price", "Not found")))
        embedstockprice.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/b/b9/Robinhood_Logo.png")
        embedstockprice.set_footer(text="{} | Financial Modeling Prep API ".format(arg))
        await ctx.send(embed=embedstockprice)

def setup(client):
    client.add_cog(StockPrice(client))