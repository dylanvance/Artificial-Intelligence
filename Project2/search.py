import matplotlib.pyplot as plt
import numpy as np
import time
import matplotlib.animation as animation
import matplotlib.path as mpath
import math

from utils import *
from grid import *

def gen_polygons(worldfilepath):
    polygons = []
    with open(worldfilepath, "r") as f:
        lines = f.readlines()
        lines = [line[:-1] for line in lines]
        for line in lines:
            polygon = []
            pts = line.split(';')
            for pt in pts:
                xy = pt.split(',')
                polygon.append(Point(int(xy[0]), int(xy[1])))
            polygons.append(polygon)
    return polygons

# Creates a path for every edge of the polygons. Used for horizontal line test
def create_paths(polygons):
    paths = []
    for polygon in polygons:
        for i in range(len(polygon)):
            start = (polygon[i].x, polygon[i].y)
            end = (polygon[(i+1)%len(polygon)].x, polygon[(i+1)%len(polygon)].y)
            path = mpath.Path([start, end], [mpath.Path.MOVETO, mpath.Path.LINETO])
            paths.append(path)
    return paths

# Horizontal line test
def is_inside(path, paths, point):
    intersections = 0
    for other_path in paths:
        if path.intersects_path(other_path, filled=True):
            intersections += 1
    """
    if paths == epaths:
        for row in epolygons:
            for vert in row:
                if vert.x > point.x and vert.y == point.y:
                    intersections += 1
    if paths == tpaths:
        for row in tpolygons:
            for vert in row:
                if vert.x > point.x and vert.y == point.y:
                    intersections += 1
    """
    return intersections % 2 == 1 # True if odd (inside), False if even (outside)

# Checks if point is an enclosure vertex, inside an enclosure, and inbounds (50, 50)
def is_valid(point):
    if not (0 <= point.x < 50 and 0 <= point.y < 50):
        return False
    temp = False
    for row in epolygons:
        for pt in row:
            if point.__eq__(pt):
                temp = True
    if temp:
        return False
    horiz = mpath.Path([(point.x, point.y), (49, point.y)], [mpath.Path.MOVETO, mpath.Path.LINETO])
    if is_inside(horiz, epaths, point):
        return False
    return True

# Calculates straight line distance with the distance formula
def get_sld(point1, point2):
    d = math.sqrt(pow((point2.x - point1.x), 2) + pow((point2.y - point1.y), 2))
    return d

def write_to_summary(cost, nodes):
    summary.write("Path Cost: ")
    summary.write(str(cost))
    summary.write("\n")
    summary.write("Nodes Expanded: ")
    summary.write(str(nodes))
    summary.write("\n")

def BFS():
    frontier = Queue()
    frontier.push(source)
    parent = {}
    parent[source] = None
    reached = []
    path = []
    cost = 0

    while not frontier.isEmpty():
        current = frontier.pop()    # Pop next point

        x = current.x
        y = current.y
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):   # Up, right, down, left
            neighbor = Point(x + dx, y + dy)    # Create new point obj

            if neighbor in reached:     # Already reached
                continue

            if not is_valid(neighbor):  # Check if in enclosure and in 50x50 grid
                continue

            frontier.push(neighbor)         # Add to frontier to goto later
            parent[neighbor] = current      # Track parent
            reached.append(neighbor)

            if neighbor.__eq__(dest):       # If dest is reached, trace through the parent dict for path
                while True:
                    horiz = mpath.Path([(neighbor.x, neighbor.y), (49, neighbor.y)],
                                       [mpath.Path.MOVETO, mpath.Path.LINETO])
                    if is_inside(horiz, tpaths, neighbor):
                        cost += 1.5
                    else:
                        cost += 1
                    if neighbor.__eq__(source):
                        path.append(neighbor)
                        break
                    path.append(neighbor)
                    neighbor = parent[neighbor]
                path.reverse()                      # Reverse the path
                write_to_summary(cost, len(reached))
                return path

    print("Error In Breadth-First Search: Could Not Find Destination")
    quit()

def DFS():
    frontier = Stack()
    frontier.push(source)
    parent = {}
    parent[source] = None
    reached = []
    path = []
    cost = 0

    while not frontier.isEmpty():
        current = frontier.pop()

        if current.__eq__(dest):
            while True:
                horiz = mpath.Path([(current.x, current.y), (49, current.y)],
                                   [mpath.Path.MOVETO, mpath.Path.LINETO])
                if is_inside(horiz, tpaths, current):
                    cost += 1.5
                else:
                    cost += 1
                if current.__eq__(source):
                    path.append(current)
                    break
                path.append(current)
                current = parent[current]
            path.reverse()
            write_to_summary(cost, len(reached))
            return path

        if current in reached:
            continue

        x = current.x
        y = current.y
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            neighbor = Point(x + dx, y + dy)

            if not is_valid(neighbor):
                continue

            if neighbor not in reached:
                frontier.push(neighbor)
                parent[neighbor] = current
        reached.append(current)

    print("Error in Depth-First Search: Could Not Find Destination")
    quit()

def GBFS():
    frontier = PriorityQueue()
    frontier.push(source, 0)
    parent = {}
    parent[source] = None
    reached = []
    path = []
    cost = 0

    while not frontier.isEmpty():
        current = frontier.pop()

        if current.__eq__(dest):
            while True:
                horiz = mpath.Path([(current.x, current.y), (49, current.y)],
                                   [mpath.Path.MOVETO, mpath.Path.LINETO])
                if is_inside(horiz, tpaths, current):
                    cost += 1.5
                else:
                    cost += 1
                if current.__eq__(source):
                    path.append(current)
                    break
                path.append(current)
                current = parent[current]
            path.reverse()
            write_to_summary(cost, len(reached))
            return path

        x = current.x
        y = current.y
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            neighbor = Point(x + dx, y + dy)

            if not is_valid(neighbor):
                continue

            heuristic = get_sld(neighbor, dest)

            if neighbor not in reached:
                frontier.push(neighbor, heuristic)
                parent[neighbor] = current
        reached.append(current)

    print("Error In Greedy Best-First Search: Could Not Find Destination")
    quit()

def ASTAR():
    frontier = PriorityQueue()
    frontier.push(source, 0)
    parent = {}
    parent[source] = None
    cost = {}
    cost[source] = 0
    path = []
    pcost = 0
    reached = []

    while not frontier.isEmpty():
        current = frontier.pop()

        if current.__eq__(dest):
            while True:
                horiz = mpath.Path([(current.x, current.y), (49, current.y)],
                                   [mpath.Path.MOVETO, mpath.Path.LINETO])
                if is_inside(horiz, tpaths, current):
                    pcost += 1.5
                else:
                    pcost += 1
                if current.__eq__(source):
                    path.append(current)
                    break
                path.append(current)
                current = parent[current]
            path.reverse()
            write_to_summary(pcost, len(reached))
            return path

        x = current.x
        y = current.y
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            neighbor = Point(x + dx, y + dy)

            if not is_valid(neighbor):
                continue

            horiz = mpath.Path([(current.x, current.y), (49, current.y)], [mpath.Path.MOVETO, mpath.Path.LINETO])
            if is_inside(horiz, tpaths, current):
                new_cost = cost[current] + 1.5
            else:
                new_cost = cost[current] + 1

            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                frontier.push(neighbor, get_sld(neighbor, dest) + new_cost)
                parent[neighbor] = current
        reached.append(current)
    print("Error In A* Search: Could Not Find Destination")
    quit()

if __name__ == "__main__":
    epolygons = gen_polygons('TestingGrid/world1_enclosures.txt')
    tpolygons = gen_polygons('TestingGrid/world1_turfs.txt')

    source = Point(8,10)
    dest = Point(43,45)

    fig, ax = draw_board()
    draw_grids(ax)
    draw_source(ax, source.x, source.y)  # source point
    draw_dest(ax, dest.x, dest.y)  # destination point
    
    # Draw enclosure polygons
    for polygon in epolygons:
        for p in polygon:
            draw_point(ax, p.x, p.y)
    for polygon in epolygons:
        for i in range(0, len(polygon)):
            draw_line(ax, [polygon[i].x, polygon[(i+1)%len(polygon)].x], [polygon[i].y, polygon[(i+1)%len(polygon)].y])
    
    # Draw turf polygons
    for polygon in tpolygons:
        for p in polygon:
            draw_green_point(ax, p.x, p.y)
    for polygon in tpolygons:
        for i in range(0, len(polygon)):
            draw_green_line(ax, [polygon[i].x, polygon[(i+1)%len(polygon)].x], [polygon[i].y, polygon[(i+1)%len(polygon)].y])

    epaths = create_paths(epolygons)
    tpaths = create_paths(tpolygons)

    res_path = []

    summary = open("summary.txt", "a")

    while True:
        print("Select A Search Algorithm")
        print("1. DFS")
        print("2. BFS")
        print("3. GBFS")
        print("4. A*")
        algo = int(input('Enter A Digit From 1 to 4: '))
        if algo == 1:
            summary.write("DFS:\n")
            res_path = DFS()
            break
        elif algo == 2:
            summary.write("BFS:\n")
            res_path = BFS()
            break
        elif algo == 3:
            summary.write("GBFS:\n")
            res_path = GBFS()
            break
        elif algo == 4:
            summary.write("ASTAR:\n")
            res_path = ASTAR()
            break
        else:
            continue

        summary.close()

    for i in range(len(res_path)-1):
        draw_result_line(ax, [res_path[i].x, res_path[i+1].x], [res_path[i].y, res_path[i+1].y])
#        plt.pause(0.1)
    
    plt.show()
