import argparse
import math
from map import Map
from action import Action
from city import City
from node import Node


def dms_to_dd(degrees, minutes, seconds, hemisphere):
      dd = degrees + minutes/60 + seconds/3600
      if hemisphere == 'S' or hemisphere == 'W':
        dd *= -1
      return dd

def read_map(file_name):

    map = Map()
    file_name = open('france.txt', 'r')
    lines = file_name.readlines()
   
    for line in lines:
        parts = line.strip().split()
        city_name = parts[0]
        longitude = dms_to_dd(int(parts[1]), int(parts[2]), int(parts[3]), (parts[4]))
        latitude = dms_to_dd(int(parts[5]), int(parts[6]), int(parts[7]), parts[8])
        city = City(city_name, longitude, latitude)

        for i in range(3, len(parts), 3):
            neighbor_city = parts[i]
            neighbor_x = map.get_city(neighbor_city)
            neighbor_y = map.get_city(neighbor_city)
            euclidean_distance = math.sqrt((longitude - neighbor_x)** + (latitude - neighbor_y)**2)

            city.add_neighbor(neighbor_city, euclidean_distance)
    
        map.add_city(city)

    return map


def write_solutions(file_name, solutions):

    with open(file_name, 'w') as file:
        for solution in solutions: 
            file.write(f"Path: {solution['path']}\n")
            file.write(f"Cost: {solution['cost']}\n")
            file.write(f"Nodes Explored: {solution['nodes_explored']}\n")
            file.write(f"Nodes Expanded: {solution['nodes_expanded']}\n")
            file.write(f"Nodes Maintained: {solution['nodes_maintained']}\n")


def main():

    parser = argparse.ArgumentParser(description= '')
    parser.add_argument('-A', required=False, help='Start city')
    parser.add_argument('-B', required=False, help='Goal city')
    parser.add_argument('-filename', required=True, help='Map file')
    parser.add_argument('-search', default='bfs', choices=['bfs', 'dls', 'ucs', 'astar'], help='Search Algorithm')
    parser.add_argument('-depth', required=False, help='Search Depth')


    args = parser.parse_args()

    map = read_map('/france.txt')

    if args.A and args.B:
        start = args.A 
        goal = args.B
        solutions = []


        if args.search == 'bfs':
            path, cost, nodes_explored, nodes_expanded, nodes_maintained = Action.bfs(map, start, goal)
            solutions.append({
                'path': path,
                'cost': cost,
                'nodes_explored': nodes_explored,
                'nodes_expanded': nodes_expanded,
                'nodes_maintained': nodes_maintained
            })

        write_solutions('README.md', solutions)

        if args.search == 'dls':
            depth = args.depth
            path, cost, nodes_explored, nodes_expanded, nodes_maintained = Action.dls(map, start, goal, depth)
            solutions.append({
                'path': path,
                'cost': cost,
                'nodes_explored': nodes_explored,
                'nodes_expanded': nodes_expanded,
                'nodes_maintained': nodes_maintained
            })

    else:

        default_city_pairs = [
            ('Brest', 'Nice'),
            ('Monteplier', 'Calais'),
            ('Strasbourg', 'Bordeux'),
            ('Paris', 'Grenoble'),
            ('Grenoble', 'Paris'),
            ('Brest','Grenoble'),
            ('Grenoble', 'Brest'),
            ('Nice', 'Nantes'),
            ('Caen', 'Strasbourg')
        ]

        solutions = [] 

        for start, goal in default_city_pairs:
            if args.search == 'bfs':
                path, cost, nodes_explored, nodes_expanded, nodes_maintained = Action.bfs(map, start, goal)
                solutions.append({
                    'path': path,
                    'cost': cost,
                    'nodes_explored': nodes_explored,
                    'nodes_expanded': nodes_expanded,
                    'nodes_maintained': nodes_maintained
                })

        write_solutions('README.md', solutions)


if __name__ == "__main__":
    main()