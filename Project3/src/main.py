from pysat.formula import CNF
from pysat.solvers import Solver
from GUI import GUI
import FileParser as fp

# Creating a dictionary where keys are 1: attr1[val1], -1: attr1[val2], ...
def create_dict():
    dict = {}
    counter = 1
    for row in attribute_list:
        dict[counter] = row[1]
        dict[-counter] = row[2]
        counter += 1
    return dict

# Creating a dictionary where keys are attr1[val1]: 1, attr1[val2]: -1, ...
def create_reverse_dict():
    dict = {}
    counter = 1
    for row in attribute_list:
        dict[row[1]] = counter
        dict[row[2]] = -counter
        counter += 1
    return dict

# Generates a list of binary numbers separated by each digit up to a certain limit.
# Used by the generate_objects() function.
# Ex: [[0, 0], [0, 1], [1, 0], [1, 1]]
def generate_binary_encoding(num_digits):
    binary_string = "1" * num_digits
    limit = int(binary_string, 2) + 1
    binary_numbers = []
    for i in range(limit):
        binary_number = []
        quotient = i
        while quotient > 0:
            binary_digit = quotient % 2
            binary_number.insert(0, binary_digit)
            quotient //= 2
        while len(binary_number) < num_digits:
            binary_number.insert(0, 0)
        binary_numbers.append(binary_number)

    return binary_numbers

# Generates a dictionary of all the possible objects, ordered with binary encoding
# Also prints them
def generate_objects():
    binaries = generate_binary_encoding(len(attribute_list))
    dict = {}
    obj_ctr = 0
    for row in binaries:
        temp_list = []
        temp_str = ""
        ctr = 1
        for i in row:
            if (i == 0):
                temp_list.append(attr_dict[-ctr])
            elif (i == 1):
                temp_list.append(attr_dict[ctr])
            ctr += 1
        temp_str = "o" + str(obj_ctr)
        obj_ctr += 1
        dict[temp_str] = temp_list

    for key in dict:
        print(str(key) + ":", end=" ")
        print(*dict[key])

    return dict

#Parses the contstraints_list and turns it into a list formatted for the CNF method from the PySAT package
def parse_constraints():
    # Splits the constraint into a list of each word
    constraints = []
    for row in constraint_list:
        row_list = row.split(" ")
        constraints.append(row_list)

    cnf_list = []

    # (1 v -1) ^ (2 v -2)... ensures that all attributes will be printed without changing meaning of formula
    for key in attr_dict:
        cnf_list.append([key, -key])

    # Parses the constraint and creates the CNF formula
    for i in range(len(constraints)):
        temp_list = []
        not_flag = False
        temp_int = 0
        for j in range(len(constraints[i])):
            if (constraints[i][j] == 'NOT'):
                not_flag = True
                continue
            elif (constraints[i][j] == 'OR'):
                continue
            elif (constraints[i][j] in reverse_dict):
                temp_int = reverse_dict[constraints[i][j]]
                if not_flag:
                    temp_int = -temp_int
                temp_list.append(temp_int)
                not_flag = False
        cnf_list.append(temp_list)

    return cnf_list

# Parses the penalty and possibilistic logic constraints and returns a dictionary with the penalties as keys mapped to their CNF formula
def parse_logic(logic_list):
    constraints = {}
    for row in logic_list:
        row_list = row[0].split()
        constraints[row[1]] = row_list

    for key in constraints:
        temp = constraints[key]
        cnf_list = []
        temp_list = []
        not_flag = False
        for i in range(len(temp)):
            temp_int = 0
            if (temp[i] == 'NOT'):
                not_flag = True
                continue
            elif (temp[i] == 'OR'):
                continue
            elif (temp[i] == 'AND'):
                cnf_list.append(temp_list)
                temp_list = []
                continue
            elif (temp[i] in reverse_dict):
                temp_int = reverse_dict[temp[i]]
                if not_flag:
                    temp_int = -temp_int
                temp_list.append(temp_int)
                not_flag = False
        cnf_list.append(temp_list)

        constraints[key] = cnf_list

    return constraints


#TODO: Finish this
def parse_qualitative_logic():
    print()


# Checks if an object is feasible based on the constraint
def is_feasible(object):

    with Solver(bootstrap_with=cnf) as solver:
        model_list = []

        for string in object:
            model_list.append(reverse_dict[string])

        satisfied = False
        for model in solver.enum_models():
            if (model == model_list):
                satisfied = True

        if not satisfied:
            return False    # Not feasible
        else:
            return True     # Feasible


# Determines the penalty of each object
# Prints the list of objects with lowest penalty
def determine_penalties():
    constraints = parse_logic(penalty_logic_list)

    lowest_objects = []
    lowest_penalty = 999
    cnfs_list = []

    for key1 in obj_dict:
        running_total = 0
        for key2 in constraints:

            if not is_feasible(obj_dict[key1]):
                running_total = 999 + 1
                continue

            cnfs_list = []

            for row in constraints[key2]:
                cnfs_list.append(row)

            for key3 in attr_dict:
                cnfs_list.append([key3, -key3])

            temp_cnf = CNF(from_clauses=cnfs_list)
            with Solver(bootstrap_with=temp_cnf) as temp_solver:
                model_list = []

                for object in obj_dict[key1]:
                    model_list.append(reverse_dict[object])

                satisfied = False
                for model in temp_solver.enum_models():
                    if (model == model_list):
                        satisfied = True

                if not satisfied:
                    running_total += key2

        if (running_total < lowest_penalty):
            lowest_objects = []
            lowest_objects.append(key1)
            lowest_penalty = running_total
        elif (running_total == lowest_penalty):
            lowest_objects.append(key1)

    print("Penalty Optimal: ")
    print(*lowest_objects, end=" ")
    print("with " + str(lowest_penalty) + " penalty")

    output = []
    for string in lowest_objects:
        output.append(string)

    output.append("with " + str(lowest_penalty) + " penalty")

    gui_results_list.append(output)

# Determines the possibilistic logic of each object
# Prints the list of most optimal objects
def determine_possibilistic():
    constraints = parse_logic(possbilistic_logic_list)

    optimal_objects = []
    highest = 0
    possiblisitic = 1
    cnfs_list = []

    for key1 in obj_dict:
        possiblisitic = 1
        object_degrees = []
        for key2 in constraints:
            possiblisitic = 1

            if not is_feasible(obj_dict[key1]):
                possiblisitic = -1
                continue

            cnfs_list = []

            for row in constraints[key2]:
                cnfs_list.append(row)

            for key3 in attr_dict:
                cnfs_list.append([key3, -key3])

            temp_cnf = CNF(from_clauses=cnfs_list)
            with Solver(bootstrap_with=temp_cnf) as temp_solver:
                model_list = []

                for object in obj_dict[key1]:
                    model_list.append(reverse_dict[object])

                satisfied = False
                for model in temp_solver.enum_models():
                    if (model == model_list):
                        satisfied = True

                if not satisfied:
                    possiblisitic -= key2
                    object_degrees.append(possiblisitic)

        object_degrees.sort()

        if (len(object_degrees) > 0):
            if (object_degrees[0] > highest):
                optimal_objects = []
                optimal_objects.append(key1)
                highest = object_degrees[0]
            elif (object_degrees[0] == highest):
                optimal_objects.append(key1)

    print("Possibilistic Optimal: ")
    print(*optimal_objects, end=" ")
    print("with " + str(highest) + " tolerance")

    output = []
    for string in optimal_objects:
        output.append(string)

    output.append("with " + str(highest) + " tolerance")

    gui_results_list.append(output)


# TODO: Finish this
def determine_qualitative_logic():
    print()


####################################### main code #################################################################


attribute_list = []
constraint_list = []
penalty_logic_list = []
possbilistic_logic_list = []
qualitative_choice_logic_list = []


gui_attribute_list = []
gui_constraint_list = []
gui_penalty_logic_list = []
gui_possbilistic_logic_list = []
gui_qualitative_choice_logic_list = []
gui_file_name_list = ["" for i in range(5)]

gui_results_list = []

def pySat_solver():
    global attr_dict
    global reverse_dict
    global obj_dict
    global cnfs
    global cnf

    attr_dict = create_dict()
    reverse_dict = create_reverse_dict()

    print("Objects: ")
    obj_dict = generate_objects()
    print()

    cnfs = parse_constraints()

    # constraint formula
    cnf = CNF(from_clauses=cnfs)

    # create a SAT solver for this formula:
    with Solver(bootstrap_with=cnf) as solver:
        # Prints feasible objects
        print('Feasible: ')
        feasible_list = []
        obj_list = []
        for m in solver.enum_models():
            print_list = []
            for i in range(len(m)):
                print_list.append(attr_dict[m[i]])

            for key in obj_dict:
                if (print_list == obj_dict[key]):
                    obj_list.append(key)

        obj_list.sort()
        for string in obj_list:
            print(string + ":", end=" ")
            print(*obj_dict[string])
            feasible_list.append(string + ": " + str(obj_dict[string]))

        gui_results_list.append(feasible_list)

    print()

    determine_penalties()

    print()

    determine_possibilistic()

def SubmitFields():
    global attribute_list
    global constraint_list
    global penalty_logic_list
    global possbilistic_logic_list
    global qualitative_choice_logic_list

    attribute_list = gui_attribute_list
    constraint_list = gui_constraint_list
    penalty_logic_list = gui_penalty_logic_list
    possbilistic_logic_list = gui_possbilistic_logic_list
    qualitative_choice_logic_list = gui_qualitative_choice_logic_list

    pySat_solver()

def SubmitFiles():
    global attribute_list
    global constraint_list
    global penalty_logic_list
    global possbilistic_logic_list
    global qualitative_choice_logic_list

    attribute_list = fp.read_attributes_file(gui_file_name_list[0])
    constraint_list = fp.read_constraints_file(gui_file_name_list[1])
    penalty_logic_list = fp.read_pentalty_file(gui_file_name_list[2])
    possbilistic_logic_list = fp.read_possbilistic_file(gui_file_name_list[3])
    qualitative_choice_logic_list = fp.read_qualitative_file(gui_file_name_list[4])

    pySat_solver()

gui = GUI(gui_attribute_list, gui_constraint_list, gui_penalty_logic_list, gui_possbilistic_logic_list, gui_qualitative_choice_logic_list, gui_file_name_list, SubmitFields, SubmitFiles, gui_results_list)

pySat_solver()