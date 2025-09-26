from character import Character

# TODO

# 1. Create an Enemy Class that inherits from the Character class
# 2. Move common functionality between the Hero and Enemy to the Character class
# 3. Creat an Item class and different items inheriting from it.


#from character import Character
# Character ___ Hero
#        |___ Enemy

class Hero (Character):
    def __init__(self):
        super().__init__() # Call the __init__ of the parent class
        print("this is the Hero Class")
    
        self.health_potion_strength = 5
        
        self.stats = {
            "name" : "hero",
            "strength": 7,
            "health": 100.0,
        }

        self.inventory = ["sword", "health potion", "rope"]
    
    def print_stats(self):
        print("Your stats are: ")
        for key,value in self.stats.items():
            print(f"{key} : {value}")

    def set_name(self, name):
        self.stats["name"] = name
        self.print_stats()

    def move(self):
        pass

    def attack(self):
        pass

    def take_damage(self, damage):
        self.stats["health"] = self.stats["health"] - damage
        print (f"Your Health is now {self.stats['health']}")
        
    def heal(self,item_name):

        #TODO -> Move this to the Use Item Function
        if (self.inventory.count("health potion") <= 0):
            print (f"You don't have any {item_name}")
            return

        print (f"You've used a {item_name} you've restored {self.health_potion_strength} Health")
        self.stats["health"] = self.stats["health"] + self.health_potion_strength

        if (self.stats["health"] >= self.max_health):
            print ("You've Reached Max Health")
            self.stats["health"] = self.max_health

        print (f"Your Health is now {self.stats['health']}")
        self.inventory.remove("health potion")
        print(f"Your inventory is now {self.inventory}")

    def use_item(self):
        pass


def main ():
    print ("This is where our program/game starts")
    #-------------------------------------------------
    hero = Hero() # <--- __init__(self)
    hero.print_stats()
    print("\n--------------------------------\n")
    hero.set_name("Omar")
    print("\n--------------------------------\n")
    hero.stats["health"] = 70
    hero.heal("health potion")
    print("\n--------------------------------\n")
    print (f"{hero.max_health}")
    hero.retreat()
    #print(f"Here are your Hero Stats {player.stats}")



if __name__ == '__main__':
    main()
