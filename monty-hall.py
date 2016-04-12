import random

def player_select_door(doors):
    return random.randint(0,len(doors)-1)

def setup_game(number_of_doors):
    # doors = ["Car"] + ['Goat' for x in range(0, number_of_doors - 1)]
    doors = ["Car"] + ['Goat' + str(x) for x in range(0, number_of_doors - 1)]
    random.shuffle(doors)
    return doors

def available_doors(doors, player_door):
    # remaining_doors = doors[:player_door] + doors[player_door+1:]
    remaining_doors = list(range(0, len(doors)))
    remaining_doors.remove(player_door)
    eligible_doors = []
    for door in remaining_doors:
        if doors[door] != "Car":
            eligible_doors.append(door)
    return eligible_doors

def get_open_door(available_doors):
    return random.choice(available_doors)

def remaining_doors(player_door, opened_door, doors):
    remaining_door = list(range(0, len(doors)))
    remaining_door.remove(player_door)
    remaining_door.remove(opened_door)
    return remaining_door[0]

def stay_or_switch_decision():
    decision = random.randint(0,1)
    if decision == 1:
        print ("Stay")
        #stay
        return True
    else:
        print("Switch")
        #switch
        return False

def play_game(number_of_doors, stay, doors, player_door, remaining_door):
    if stay:
        if doors[player_door] == "Car":
            print ("winner!")
            return True
        else:
            print ("loser!")
            return False
    else:
        if doors[remaining_door] == "Car":
            print ("winner!")
            return True
        else:
            print ("loser!")
            return False

def play_game_stay(doors, player_door):
    if doors[player_door] == "Car":
        # print ("winner!")
        return True
    else:
        # print ("loser!")
        return False

def play_game_switch(doors, remaining_door):
   if doors[remaining_door] == "Car":
       return True
   else:
       return False
    # return t/f if they win or not

def main():
    stay_counter = 0
    switch_counter = 0

    for _ in range(1000):
        doors = setup_game(3)
        player_door = player_select_door(doors)
        available_door = available_doors(doors, player_door)
        opened_door = get_open_door(available_door)

        if play_game_switch(doors, remaining_doors(player_door, opened_door, doors)):
            switch_counter += 1

        if play_game_stay(doors, player_door):
            stay_counter += 1

    print ("Stay: ", stay_counter)
    print ("Switch: ", switch_counter)


if __name__ == '__main__':
    main()
