import random

games = []

class NumGame():
    def __init__(self):
        self.target_num = 0
        self.num_of_guesses = 4
        self.player_guess = 0
        self.endgame = False
        self.did_guess = False

    async def game(self, ctx, client):
        await ctx.send("welcome to the number guessing game! the rules are simple. you get 4 attempts to guess the "
                       "number from 1 to 20. type \"**stop**\" to quit the game. \ngood luck!")
        self.target_num = int(random.randrange(1, 20))
        for x in range(self.num_of_guesses+1):
            while True:
                self.player_guess = await client.wait_for("message")
                try:
                    self.player_guess = int(self.player_guess.content)
                    break
                except ValueError:
                    if str(self.player_guess.content).lower() == "stop":
                        self.endgame = True
                        break
                    else:
                        await ctx.send("not a valid guess. please enter a valid .")
                        continue
            if self.endgame:
                break
            else:
                if self.player_guess == self.target_num:
                    self.did_guess = True
                    break
                elif self.player_guess > self.target_num:
                    await ctx.send(f"too high! you have {self.num_of_guesses - x} guesses left")
                elif self.player_guess < self.target_num:
                    await ctx.send(f"too low! you have {self.num_of_guesses - x} guesses left")

        if self.endgame:
            await ctx.send("game ended by player. see you next time!")
        else:
            if self.did_guess:
                await ctx.send(f"you won! the number was {self.target_num}")
            else:
                await ctx.send(f"better luck next time :( the number was {self.target_num}")
