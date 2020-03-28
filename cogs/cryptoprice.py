from discord.ext import commands
import discord
import requests

class CryptoPrice(commands.Cog):

    def init(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print("CryptoPrice Loaded!")

    @commands.command(pass_context=True)
    async def cryptoprice(self, ctx, *, arg):

        ticker = requests.get("https://financialmodelingprep.com/api/v3/cryptocurrency/{}".format(arg)).json()
        price = requests.get("https://financialmodelingprep.com/api/v3/cryptocurrency/{}".format(arg)).json()

        embedstockprice = discord.Embed(title="Cryptocurrency Price", color=discord.Color(0x21CE99))
        embedstockprice.add_field(name="Symbol", value="{}".format(ticker.get("ticker", "Not found")))
        embedstockprice.add_field(name="Price", value ="${}".format(price.get("price", "Not found")))
        embedstockprice.set_thumbnail(url="https://is2-ssl.mzstatic.com/image/thumb/Purple124/v4/80/fd/3c/80fd3c3a-08e9-c5d9-cfb0-bda3d821209c/AppIcon-0-1x_U007emarketing-0-0-GLES2_U002c0-512MB-sRGB-0-0-0-85-220-0-0-0-5.png/1024x1024bb.jpg")
        embedstockprice.set_footer(text="{} | Financial Modeling Prep API ".format(arg))
        await ctx.send(embed=embedstockprice)

def setup(client):
    client.add_cog(CryptoPrice(client))