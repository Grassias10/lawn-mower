class Player:
    def __init__(self, m):
        self.lives = 3
        self.msg_obj = m

    def getLives(self):
        return self.lives

    def getMsgObj(self):
        return self.msg_obj

    def lifeLoss(self):
        self.lives -= 1
        print(f"{self.msg_obj.author.name} has {self.lives} lives")

    def isAlive(self):
        if self.lives <= 0:
            return False
        else:
            return True
