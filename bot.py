import discord, json
from discord.ext import commands
from datetime import datetime
import blowupbash as bub

inte = discord.Intents.all()
bot = commands.Bot(command_prefix='...', intents=inte)


@bot.event
async def on_ready():
    print("Starting up bot!")


@bot.command(name="github", aliases=["git"])
async def github(ctx):
    await ctx.send("https://github.com/TheFlyingJeep/blow-up-bash")


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


@bot.command(name="time", aliases=["currenttime"])
async def time(ctx):
    today = datetime.now()
    ct = today.strftime("%I:%M")
    ampm = ""
    if int(today.strftime("%H")) < 12:
        ampm = "am"
    else:
        ampm = "pm"
    await ctx.send("current time (EDT): " + ct + ampm)

@bot.command(name="date", aliases=["currentdate"])
async def time(ctx):
    d = str(datetime.now())
    date = d.split(" ")
    await ctx.send("today's date (yyyy-mm-dd): " + date[0])

if __name__ == "__main__":
    with open("secrets.json") as sec:
        data = json.load(sec)
        bot.run(data["token"])
