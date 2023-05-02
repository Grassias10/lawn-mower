import random

games = []

class NumGame():
    def __init__(self):
        self.target_num = 0
        self.num_of_guesses = 4
        self.player_guess = 0
        self.endgame = False
        self.did_guess = False
        self.player_id = 0

    async def setPlayerId(self, p_id):
        self.player_id = p_id

    async def game(self, ctx, client):
        await ctx.send("welcome to the number guessing game! the rules are simple. you get 4 attempts to guess the "
                       "number from 1 to 20. type \"**stop**\" to quit the game. \ngood luck!")
        self.target_num = int(random.randrange(1, 20))
        print(self.target_num)

        def checkMsg(p):
            return p.channel == ctx.channel and p.author.id == self.player_id

        for x in range(self.num_of_guesses+1):
            await ctx.send("guess a number from 1 to 20:")
            try:
                msg = await client.wait_for("message", check=checkMsg)
                self.player_guess = int(msg.content)
                if self.player_guess == self.target_num:
                    await ctx.send(f"you won! the number was {self.target_num}")
                    break
                elif self.player_guess > self.target_num:
                    await ctx.send(f"too high! you have {self.num_of_guesses - x} guesses left")
                elif self.player_guess < self.target_num:
                    await ctx.send(f"too low! you have {self.num_of_guesses - x} guesses left")
            except ValueError:
                await ctx.send("not a valid guess. please enter a valid guess.")

        if self.endgame:
            await ctx.send("game ended by player. see you next time!")
        else:
            if self.did_guess:
                await ctx.send(f"you won! the number was {self.target_num}")
            else:
                await ctx.send(f"better luck next time :( the number was {self.target_num}")
