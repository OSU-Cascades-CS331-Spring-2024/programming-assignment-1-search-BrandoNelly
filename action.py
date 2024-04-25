class Action():

    
    def bfs(map, start, goal):


        paths = {start: []}
        distances = {start: 0}

        frontier = [start]
        explored = set()

        nodes_explored = 0
        nodes_expanded = 0
        nodes_maintained = 1
        
        while not frontier.empty():
            current_city = frontier.dequeue()
            nodes_explored += 1
            nodes_maintained -= 1

            if current_city == goal:
                path = paths[current_city] + [current_city]
                cost = distances[current_city]
                return path, cost, nodes_explored, nodes_expanded, nodes_maintained
            
            explored.add(current_city)

            for neighbor_city in map.get_city(current_city).get_neighbors():
                nodes_expanded += 1

                if neighbor_city not in explored and neighbor_city not in frontier:
                    frontier.append(neighbor_city)
                    nodes_maintained += 1


                    paths[neighbor_city] = paths[current_city] + {current_city}
                    distances[neighbor_city] = distances[current_city] + map.get_city(current_city).neighbors[neighbor_city]

        return path, cost, nodes_explored, nodes_expanded, nodes_maintained



    def dls(problem, limit):

        paths = {problem.start: []}
        distances = {problem.start: 0}

        frontier = [problem.start]
        explored = set()

        nodes_explored = 0
        nodes_expanded = 0
        nodes_maintained = 1

        while frontier:
            current_city, depth = frontier.dequeue()
            nodes_explored += 1
            nodes_maintained -= 1


            if current_city == problem.goal:
                path = paths[current_city] + [current_city]
                cost = distances[current_city]
                return path, cost, nodes_explored, nodes_expanded, nodes_maintained
            
            if depth < limit:
                explored.add(current_city)

                for neighbor_city in map.get_city(current_city).get_neighbors():
                    nodes_expanded += 1

                    if neighbor_city not in explored and neighbor_city not in frontier:
                        frontier.append((neighbor_city, depth + 1))
                        nodes_maintained += 1

        return path, cost, nodes_explored, nodes_expanded, nodes_maintained


        
    # def ucs(map, start, goal):

        
    # def astar(map, start, goal):