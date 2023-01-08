import discord
import os
import random
from dotenv import load_dotenv
from discord.ext import commands

client = commands.Bot(command_prefix="...", intents=discord.Intents.all())


@client.command()
async def ping(ctx):
    await ctx.send("pong!")


@client.command()
async def game(ctx):
    await ctx.send("welcome to the number guessing game! the rules are simple. "
                   "you get 4 attempts to guess the number from 1 to 20. type \"stop\" to quit the game. "
                   "good luck!")
    num = int(random.randrange(1, 20))
    didguess = False
    numofguesses = 4
    endgame = False

    for x in range(numofguesses+1):
        while True:
            playerguess = await client.wait_for("message")
            try:
                playerguess = int(playerguess.content)
                break
            except ValueError:
                if str(playerguess.content).lower() == "stop":
                    endgame = True
                    break
                else:
                    await ctx.send("not a valid guess. try again.")
                    continue

        if endgame:
            break
        else:
            if playerguess == num:
                didguess = True
                break
            elif playerguess > num:
                await ctx.send(f"too high! you have {numofguesses - x} guesses left")
            elif playerguess < num:
                await ctx.send(f"too low! you have {numofguesses - x} guesses left")

    if endgame:
        await ctx.send("game ended by player. see you next time!")
    else:
        if didguess:
            await ctx.send(f"you won! the number was {num}")
        else:
            await ctx.send(f"better luck next time :( the number was {num}")


class MyHelpCommand(commands.HelpCommand):
    async def send_bot_help(self, mapping):
        embed = discord.Embed(title="help", color=discord.Color.green())
        embed.add_field(name="help - this command")
        embed.add_field(name="ping")
        embed.add_field(name="game - number guessing game")

        channel = self.get_destination()
        await channel.send(embed=embed)


load_dotenv()
token = os.getenv("TOKEN")
client.run(token)
