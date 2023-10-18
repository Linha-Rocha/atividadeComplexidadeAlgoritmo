import numpy as np
from python_tsp.exact import solve_tsp_dynamic_programming
import json

#Fórmula de haversine
def haversine_distance(coord1, coord2):
    R = 6371.0  # Raio terrestre em kilometros
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    
    dlat = np.radians(lat2 - lat1)
    dlon = np.radians(lon2 - lon1)
    
    a = (np.sin(dlat / 2) * np.sin(dlat / 2) +
         np.cos(np.radians(lat1)) * np.cos(np.radians(lat2)) *
         np.sin(dlon / 2) * np.sin(dlon / 2))
    
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    distance = R * c
    return distance

# Lendo o arquivo pedidos.json com a codificação 'utf-8'
with open("pedidos.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Criando a matriz de localizações
locations = [data['localizacao']]
destinatarios = ["McDonalds"]  # Lista para armazenar os destinatários, começando com o nome do estabelecimento
for entrega in data['entregas']:
    locations.append(entrega['localizacao'])
    destinatarios.append(entrega['destinatario'])

# Calculando a matriz de distâncias usando Haversine
num_locations = len(locations)
distance_matrix = np.zeros((num_locations, num_locations))
for i in range(num_locations):
    for j in range(num_locations):
        distance_matrix[i, j] = haversine_distance(locations[i], locations[j])

permutation, distance = solve_tsp_dynamic_programming(distance_matrix)

# Exibindo a melhor rota usando o campo "destinatario"
print("Melhor rota:")
route = " -> ".join([destinatarios[i] for i in permutation]) + " -> " + destinatarios[0]  # Adicionando o nome do estabelecimento ao final
print(route)

# Informando a distância total
print("\nDistância total da rota: {:.2f} km".format(distance))
