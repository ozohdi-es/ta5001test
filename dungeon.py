
hero_stats = {
    "name" : "hero", # key : value (name -> key) : (hero -> value)
    "strength" : 7,
    "health" : 100.0,
}

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

isPlaying = True

hero_stats["name"] = input ("What is your name?\n")    
player_stats()

while (isPlaying):    

    action = input ("\nSelect Action: Attack, Move or Flee\n").lower()

    print (f"Player Action: {action}")

    if (action == "flee"):
        isPlaying = quit() #<-- isPlaying = False
    elif (action == "attack"):
        player_attack()
    elif (action == "move"):
        player_move()
    else:
        print (f"{action} is an invalid action")