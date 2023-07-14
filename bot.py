import discord
import json
import requests
import random
from discord.ext import commands
from datetime import datetime
from bs4 import BeautifulSoup
import blowupbash as bub
import numgame as ng


inte = discord.Intents.all()
bot = commands.Bot(command_prefix='%', intents=inte)


shitposts = []
def load_shitposts():
    r = requests.get("https://www.pinterest.com/Grassias10/poop-post/")
    soup = BeautifulSoup(r.text, "html.parser")
    for item in soup.find_all("img"):
        shitposts.append(item["src"])


@bot.event
async def on_ready():
    load_shitposts()
    print("bot started!")


@bot.command(name="github", aliases=["git"])
async def github(ctx):
    await ctx.send("https://github.com/Grassias10/lawn-mower")


@bot.event
async def on_message(msg):
    if msg.content.lower() == "join":
        await bub.addPlayers(msg)
    await bot.process_commands(msg)


@bot.command(name="blowupbash", aliases=["bub"])
async def blowupbash(ctx):
    bubgame = bub.BlowUpBash()
    bub.games.append(bubgame)
    await bubgame.game(ctx, bot)


@bot.command(name="today", aliases=["currenttime", "currentdate", "datetime", "timedate", "dt", "td"])
async def today(ctx):
    today = datetime.now()
    ct = today.strftime("%I:%M")
    ampm = ""
    if int(today.strftime("%H")) < 12:
        ampm = "am"
    else:
        ampm = "pm"
    d = str(datetime.now())
    date = d.split(" ")
    await ctx.send("today is " + date[0] + " (yyyy-mm-dd). it is currently " + ct + ampm + " (EDT).")


@bot.command(name="date", aliases=["d"])
async def date(ctx):
    d = str(datetime.now())
    date = d.split(" ")
    await ctx.send("today is " + date[0] + " (yyyy-mm-dd).")


@bot.command(name="time", aliases=["t"])
async def time(ctx):
    today = datetime.now()
    ct = today.strftime("%I:%M")
    ampm = ""
    if int(today.strftime("%H")) < 12:
        ampm = "am"
    else:
        ampm = "pm"
    await ctx.send("it is currently " + ct + ampm + " (EDT).")


@bot.command(name="numgame", aliases=["numguess"])
async def numgame(ctx):
    ngame = ng.NumGame()
    ng.games.append(ngame)
    await ngame.setPlayerId(ctx.author.id)
    await ngame.game(ctx, bot)


@bot.command(name="shitpost", aliases=["sp", "shitposts", "pooppost"])
async def shitpost(ctx):
    await ctx.send(shitposts[int(random.randrange(0, len(shitposts)))])


#@bot.command(name="ror", aliases=["roritem"])
#async def ror(ctx):


if __name__ == "__main__":
    with open("secrets.json") as sec:
        data = json.load(sec)
        bot.run(data["token"])
