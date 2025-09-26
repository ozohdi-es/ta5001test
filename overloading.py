class Character ():
    def __init__ (self):
        pass

    def move (self):
        print("Character is moving")
        pass

class Hero (Character):
    
    def __init__ (self):
        super().__init__()
        pass


class Enemy (Character):
    def __init__ (self):
        super().__init__()
        pass

    def move(self):
        print ("Enemy is moving")

Char = Character()
Char.move()
Player = Hero()
Player.move()
Goblin = Enemy()
Goblin.move()



