# TODO 
#    1. Assign hero variables for: 
    #  attack moves
    #  & their damage values,
    #  inventory.​
#    2. Track monsters & their health: goblin:30, dragon: 200 etc.​
#    3. Display hero & monster stats at the start.​
#    
#    4. Allow for inputs & functions for:​
        #    Attacking​
        #    Using an item​
#    5. Create a graphical grid representation of the world, with the player's position indicated, add a MOVE input to move the player's position on the grid.​



hero_stats = {
    "name" : "hero", # key : value (name -> key) : (hero -> value)
    "strength" : 7,
    "health" : 100.0,
}
hero_max_health = 100.0

health_potion_strength = 5
hero_inventory = ["sword","health potion", "rope"] 

def quit ():
    print ("You Chose To Flee")
    print ("GAME OVER")
    return False

def player_stats ():
    print ("You are:")
    for key, value in hero_stats.items():
        print(f"{key} : {value}" )

def player_move():
    pass

def player_attack():
    pass

def player_heal(item_name):

    if (hero_inventory.count("health potion") <= 0):
        print (f"You don't have any {item_name}")    
        return

    print (f"You've used a {item_name} you've restored {health_potion_strength} Health")
    hero_stats["health"] = hero_stats["health"] + health_potion_strength

    # TODO
    # Make sure that if the player has 100 health and they try to use a potion, 
    # The potion does not get consumed.

    # Health = 100.0
    # use Health Potions
    # print -> you're already at max health. 
    # DO NOT remove the health potion.

    if (hero_stats["health"] >= hero_max_health):
        print ("You've reached Max health")
        hero_stats["health"] = hero_max_health

    print (f"Your Health is now {hero_stats['health']}")
    hero_inventory.remove("health potion")
    print(f"Your inventory is now {hero_inventory}")

    # make sure it doesn't go above max health

def use_item():
    item_name = input(f"What item do you want to use? {hero_inventory}\n").lower()
    print (f"The item you want to use is {item_name}")
    
    match item_name: #("Map")
        case "sword":
            pass
        case "health potion":
           player_heal(item_name)
        case "rope":
            pass
        case _:
            print(f"{item_name} is not in your invetory")

# Temporary Function
def damage_player():
    hero_stats["health"] = hero_stats["health"] - 10
    print (f"Your Health is now {hero_stats['health']}")
    

isPlaying = True

hero_stats["name"] = input("What is your name?\n")    
player_stats()

while (isPlaying):    

    action = input("\nSelect Action: Attack, Move, Use or Flee\n").lower()
    print (f"Player Action: {action}")

    if (action == "flee"):
        isPlaying = quit() #<-- isPlaying = False
    elif (action == "attack"):
        #player_attack()
        damage_player() # temporary
    elif (action == "use"):
        use_item()
    elif (action == "move"):
        player_move()
    else:
        print (f"{action} is an invalid action")