import json
import math

def load_data(filename='pedidos.json'):
    """
    Load delivery data from JSON file.
    Returns:
    - starting point (estabelecimento)
    - list of deliveries with id and localizacao.
    """
    with open(filename, 'r') as file:
        data = json.load(file)
    return data['estabelecimento'], data['entregas']

def nearest_neighbor_algorithm(start, deliveries):
    """
    Solve TSP using the Nearest Neighbor heuristic.
    Returns:
    - path (route) as a list of coordinates.
    """
    unvisited = deliveries[:]
    current_location = start
    path = [start]

    while unvisited:
        nearest = min(unvisited, key=lambda x: math.dist(current_location, x['localizacao']))
        path.append(nearest['localizacao'])
        current_location = nearest['localizacao']
        unvisited.remove(nearest)

    path.append(start)  # Return to starting point
    return path

#CALCULA A DISTANCIA TOTAL#
def calculate_total_distance(route): 
    return sum(math.dist(route[i], route[i+1]) for i in range(len(route)-1))

def main():
    start, deliveries = load_data()
    route = nearest_neighbor_algorithm(start, deliveries)
    print("Rota:", route)
    print("Distância total da rota:", calculate_total_distance(route))

if __name__ == '__main__':
    main()
