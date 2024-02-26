# Pokemon Colosseum Project
# Authored by Dylan Vance
# For Dr. Liu's Intro to AI
from Pokemon import Pokemon
import random
import csv
import math


# This function parses pokemon-data.csv and creates a 2D array of all the information in the file.
# It returns the 2D Pokemon array.
def get_pokemon_data():
    records = []

    with open('pokemon-data.csv', 'r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            records.append(row)

    return records


# This functions exactly the same as get_pokemon_data but parses moves-data.csv instead.
# It returns the 2D moves array.
def get_move_data():
    records = []

    with open('moves-data.csv', 'r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            records.append(row)

    return records


# This function instantiates three Pokemon based on the numbers passed.
# It uses those numbers to index the Pokemon List to retrieve the Pokemon's stats for creation.
# It is used for the random allocation of Pokemon to each team.
# It returns the list of Pokemon.
def get_pokemon_queue(num1, num2, num3):
    pokemon1 = Pokemon(pokemon_list[num1][0], pokemon_list[num1][1], pokemon_list[num1][2], pokemon_list[num1][3],
                       pokemon_list[num1][4], pokemon_list[num1][5], pokemon_list[num1][6])

    pokemon2 = Pokemon(pokemon_list[num2][0], pokemon_list[num2][1], pokemon_list[num2][2], pokemon_list[num2][3],
                       pokemon_list[num2][4], pokemon_list[num2][5], pokemon_list[num2][6])

    pokemon3 = Pokemon(pokemon_list[num3][0], pokemon_list[num3][1], pokemon_list[num3][2], pokemon_list[num3][3],
                       pokemon_list[num3][4], pokemon_list[num3][5], pokemon_list[num3][6])

    queue = [pokemon1, pokemon2, pokemon3]

    return queue


# This function returns the type efficiency when given the attacker and defender types.
# The type_table is the table given in the instructions applied to a 2D array.
# It returns the type efficiency number used for damage calculation.
def get_type_efficiency(att_type, def_type):
                # Normal, Fire, Water, Electric, Grass
    type_table = [[1, 1, 1, 1, 1],                      # Normal
                  [1, 0.5, 0.5, 1, 2],                  # Fire
                  [1, 2, 0.5, 1, 0.5],                  # Water
                  [1, 1, 2, 0.5, 0.5],                  # Electric
                  [1, 0.5, 2, 1, 0.5],                  # Grass
                  [1, 1, 1, 1, 1]]                      # Other

    if att_type == "Normal":
        num1 = 0
    elif att_type == "Fire":
        num1 = 1
    elif att_type == "Water":
        num1 = 2
    elif att_type == "Electric":
        num1 = 3
    elif att_type == "Grass":
        num1 = 4
    else:
        num1 = 0    # This is just to be safe

    if def_type == "Normal":
        num2 = 0
    elif def_type == "Fire":
        num2 = 1
    elif def_type == "Water":
        num2 = 2
    elif def_type == "Electric":
        num2 = 3
    elif def_type == "Grass":
        num2 = 4
    else:
        num2 = 0    # This is just to be safe

    return type_table[num1][num2]


# This function calculates the damage of a given move using the damage formula.
# It takes in the move as a string as well as the Pokemon objects of the attacker and defender.
# It returns the damage value rounded up to the nearest whole number.
def get_damage(move, attacker, defender):
    i = 0
    while True:
        if moves_list[i][0] == move:
            move_power = int(moves_list[i][5])
            if moves_list[i][1] == attacker.type:
                stab = 1.5
            else:
                stab = 1
            break
        i += 1
    att = attacker.attack
    defe = defender.defense
    type_eff = get_type_efficiency(attacker.type, defender.type)
    random_list = [0.5, 0.6, 0.7, 0.8, 0.9, 1]
    r = random.randint(0, 5)
    random_val = random_list[r]

    damage = move_power * (att/defe) * stab * type_eff * random_val

    return math.ceil(damage)


# This is the function used to simulate the battle when the player moves first.
# It returns nothing
def player_attacks_first(player_team, grunt_team):
    # Popping the first Pokemon
    player_pokemon = player_team.pop(0)
    grunt_pokemon = grunt_team.pop(0)
    # Battle loop
    battle = True
    while battle:
        # Player's move code
        # Temp list used for removing moves
        temp_moves = player_pokemon.moves
        print("Select A Move For " + player_pokemon.name)
        # Makes sure to print the correct number of moves to avoid index out of bounds
        num_moves = len(player_pokemon.moves)
        if num_moves == 0:
            temp_moves = player_pokemon.moves
        if num_moves >= 1:
            print("1. " + temp_moves[0])
        if num_moves >= 2:
            print("2. " + temp_moves[1])
        if num_moves >= 3:
            print("3. " + temp_moves[2])
        if num_moves >= 4:
            print("4. " + temp_moves[3])
        if num_moves >= 5:
            print("5. " + temp_moves[4])
        # While loop / try block for error handling input
        while True:
            try:
                move = int(input("Your Selection: "))
                if 1 <= move <= 5:
                    break
                else:
                    print("Invalid Input")
            except ValueError:
                print("Invalid Input")
        move = int(move)
        move -= 1
        print("")
        # Print/Call damage code
        print(player_pokemon.name + " casts " + temp_moves[move] + " on " + grunt_pokemon.name)
        damage = get_damage(temp_moves[move], player_pokemon, grunt_pokemon)
        grunt_pokemon.hp -= damage
        print("Damage to " + grunt_pokemon.name + " is " + str(damage))
        # Determine if a Pokemon has fainted
        if grunt_pokemon.hp <= 0:
            print(grunt_pokemon.name + " has fainted!\n")
            if len(grunt_team) == 0:
                print("Grunt is out of usable pokemon\n")
                print(player + " wins!")
                break
            grunt_pokemon = grunt_team.pop(0)       # Pop next Pokemon
            print("Team Rocket Grunt sends out " + grunt_pokemon.name + "\n")
        else:
            print(grunt_pokemon.name + "'s HP is now " + str(grunt_pokemon.hp) + "\n")
        # Delete the used move
        del temp_moves[move]

        # Grunt's move code
        # Random int for random move
        grunt_move = random.randint(0, 4)
        print(grunt_pokemon.name + " casts " + grunt_pokemon.moves[grunt_move] + " on " + player_pokemon.name)
        grunt_damage = get_damage(grunt_pokemon.moves[grunt_move], grunt_pokemon, player_pokemon)
        player_pokemon.hp -= grunt_damage
        print("Damage to " + player_pokemon.name + " is " + str(grunt_damage))
        # Determine if Pokemon has fainted
        if player_pokemon.hp <= 0:
            print(player_pokemon.name + " has fainted!\n")
            if len(player_team) == 0:
                print(player + " is out of usable pokemon")
                print(player + " blacked out!\n")
                print("Game Over!")
                break
            player_pokemon = player_team.pop(0)     # Pop next Pokemon
            print(player + " sends out " + player_pokemon.name + "\n")
        else:
            print(player_pokemon.name + "'s HP is now " + str(player_pokemon.hp) + "\n")


# This is the function used to simulate the battle when the grunt moves first.
# It returns nothing
def grunt_attacks_first(player_team, grunt_team):
    # Popping the first Pokemon
    player_pokemon = player_team.pop(0)
    grunt_pokemon = grunt_team.pop(0)
    # Battle loop
    battle = True
    while battle:
        # Grunt's move code
        # Random int for random move
        grunt_move = random.randint(0, 4)
        print(grunt_pokemon.name + " casts " + grunt_pokemon.moves[grunt_move] + " on " + player_pokemon.name)
        grunt_damage = get_damage(grunt_pokemon.moves[grunt_move], grunt_pokemon, player_pokemon)
        player_pokemon.hp -= grunt_damage
        print("Damage to " + player_pokemon.name + " is " + str(grunt_damage))
        # Determine if Pokemon has fainted
        if player_pokemon.hp <= 0:
            print(player_pokemon.name + " has fainted!\n")
            if len(player_team) == 0:
                print(player + " is out of usable pokemon")
                print(player + " blacked out!\n")
                print("Game Over!")
                break
            player_pokemon = player_team.pop(0)  # Pop next Pokemon
            print(player + " sends out " + player_pokemon.name + "\n")
        else:
            print(player_pokemon.name + "'s HP is now " + str(player_pokemon.hp) + "\n")

        # Player's move code
        # Temp list used for removing moves
        temp_moves = player_pokemon.moves
        print("Select A Move For " + player_pokemon.name)
        # Makes sure to print the correct number of moves to avoid index out of bounds
        num_moves = len(player_pokemon.moves)
        if num_moves == 0:
            temp_moves = player_pokemon.moves
        if num_moves >= 1:
            print("1. " + temp_moves[0])
        if num_moves >= 2:
            print("2. " + temp_moves[1])
        if num_moves >= 3:
            print("3. " + temp_moves[2])
        if num_moves >= 4:
            print("4. " + temp_moves[3])
        if num_moves >= 5:
            print("5. " + temp_moves[4])
        # While loop / try block for error handling input
        while True:
            try:
                move = int(input("Your Selection: "))
                if 1 <= move <= 5:
                    break
                else:
                    print("Invalid Input")
            except ValueError:
                print("Invalid Input")
        move = int(move)
        move -= 1
        print("")
        # Print/Call damage code
        print(player_pokemon.name + " casts " + temp_moves[move] + " on " + grunt_pokemon.name)
        damage = get_damage(temp_moves[move], player_pokemon, grunt_pokemon)
        grunt_pokemon.hp -= damage
        print("Damage to " + grunt_pokemon.name + " is " + str(damage))
        # Determine if a Pokemon has fainted
        if grunt_pokemon.hp <= 0:
            print(grunt_pokemon.name + " has fainted!\n")
            if len(grunt_team) == 0:
                print("Grunt is out of usable pokemon\n")
                print(player + " wins!")
                break
            grunt_pokemon = grunt_team.pop(0)  # Pop next Pokemon
            print("Team Rocket Grunt sends out " + grunt_pokemon.name + "\n")
        else:
            print(grunt_pokemon.name + "'s HP is now " + str(grunt_pokemon.hp) + "\n")
        # Delete the used move
        del temp_moves[move]


# Main Code
print('         POKEMON COLOSSEUM           ')
player = input('What is your name?\n')
print('\n!')
print('Team Rocket Grunt Has Challenged You To A Battle ! ! !\n')

# Generate Pokemon List
pokemon_list = get_pokemon_data()

# Generate Pokemon Queues
randoms = random.sample(range(1, 82), 6)
playerTeam = get_pokemon_queue(randoms[0], randoms[1], randoms[2])
rocketTeam = get_pokemon_queue(randoms[3], randoms[4], randoms[5])

# Generate the List of Moves and their Info
moves_list = get_move_data()

print("Team Rocket Grunt Enters With " + rocketTeam[0].name + ", " + rocketTeam[1].name + ", and " + rocketTeam[2].name)
print()
print(player + " Enters With " + playerTeam[0].name + ", " + playerTeam[1].name + ", and " + playerTeam[2].name + "\n")

# Determine which player will attack first (coin flip)
turn = random.randint(0, 1)
if turn == 0:
    print(player + " Will Attack First\n")
    player_attacks_first(playerTeam, rocketTeam)
else:
    print("Team Rocket Grunt Will Attack First\n")
    grunt_attacks_first(playerTeam, rocketTeam)
