import csv
import ast


# This function gets the Pokemon's moves to apply to its moves list based on its name.
# Code from example_parse.py provided by Dr. Liu.
# It returns the list of moves for the Pokemon passed to it.
def get_moves(pokemon_name):
    pokemon_filename = 'pokemon-data.csv'

    header = []
    pokemon_moves = {}

    return_moves = []

    with open(pokemon_filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)

        for row in reader:
            moves = ''
            end_of_moves = False
            for s in row:
                if s[0] == '[':
                    end_of_moves = True
                    moves = s
                elif end_of_moves:
                    moves += ','+s
                    if s[-1] == ']':
                        end_of_moves = False
            pokemon_moves[row[0]] = ast.literal_eval(moves)  # string to list

    return_moves = pokemon_moves[pokemon_name]

    return return_moves


# Pokemon class.
# Only one function which is the constructor.
# Must be given all info for the Pokemon.
class Pokemon:
    def __init__(self, in_name, in_type, in_hp, in_att, in_def, in_height, in_weight):
        self.name = in_name
        self.type = in_type
        self.hp = int(in_hp)
        self.attack = int(in_att)
        self.defense = int(in_def)
        self.height = int(in_height)
        self.weight = int(in_weight)
        self.moves = get_moves(self.name)
