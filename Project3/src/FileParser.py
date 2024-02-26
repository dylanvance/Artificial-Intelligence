def read_attributes_file(fileRoute):
    res = []

    def lineToAttribute(line):
        split_line = line.split(":")
        attribute_name = split_line[0]

        values = split_line[1].strip().split(",")

        return (attribute_name, values[0].strip(), values[1].strip())

    # Open the file for reading
    file = open(fileRoute, "r")

    # Read the first line from the file
    line = file.readline()

    # Loop through the file and read each line
    while line:
        res.append(lineToAttribute(line.strip()))

        # Read the next line from the file
        line = file.readline()

    # Close the file
    file.close()

    return res

def read_constraints_file(fileRoute):
    res = []

    # Open the file for reading
    file = open(fileRoute, "r")

    # Read the first line from the file
    line = file.readline()

    # Loop through the file and read each line
    while line:
        res.append(line.strip())

        # Read the next line from the file
        line = file.readline()

    # Close the file
    file.close()

    return res

def read_pentalty_file(fileRoute):
    res = []

    # Open the file for reading
    file = open(fileRoute, "r")

    # Read the first line from the file
    line = file.readline()

    # Loop through the file and read each line
    while line:
        # Do something with the line
        values = line.strip().split(",")
        values[0] = values[0].strip()
        values[1] = int(values[1].strip())

        res.append(tuple(values))

        # Read the next line from the file
        line = file.readline()

    # Close the file
    file.close()

    return res

def read_possbilistic_file(fileRoute):
    res = []

    # Open the file for reading
    file = open(fileRoute, "r")

    # Read the first line from the file
    line = file.readline()

    # Loop through the file and read each line
    while line:
        # Do something with the line
        values = line.strip().split(",")
        values[0] = values[0].strip()
        values[1] = float(values[1].strip())

        res.append(tuple(values))

        # Read the next line from the file
        line = file.readline()

    # Close the file
    file.close()

    return res

def read_qualitative_file(fileRoute):
    res = []

    # Open the file for reading
    file = open(fileRoute, "r")

    # Read the first line from the file
    line = file.readline()

    # Loop through the file and read each line
    while line:
        res.append(line.strip())

        # Read the next line from the file
        line = file.readline()

    # Close the file
    file.close()

    return res

'''
Used for testing
Only runs when this file is run directly as opposed to being imported
'''
if __name__ == "__main__":
    print("Attributes test: ")
    print(read_attributes_file("./Instructions/ExampleCase/attributes.txt"))

    print()

    print("Constraint test: ")
    print(read_constraints_file("./Instructions/ExampleCase/constraints.txt"))

    print()

    print("Pentalty test: ")
    print(read_pentalty_file("./Instructions/ExampleCase/penaltylogic.txt"))

    print()

    print("Possbilistic test: ")
    print(read_possbilistic_file("./Instructions/ExampleCase/possibilisticlogic.txt"))

    print()

    print("Qualitative test: ")
    print(read_qualitative_file("./Instructions/ExampleCase/qualitativechoicelogic.txt"))
