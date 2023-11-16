import json

import numpy as np
from python_tsp.exact import solve_tsp_dynamic_programming

from avl_tree import AVLTree
from pedido import Pedido


# Fórmula de haversine
def haversine_distance(coord1, coord2):
    r = 6371.0  # Raio terrestre em kilometros
    lat1, lon1 = coord1
    lat2, lon2 = coord2

    dlat = np.radians(lat2 - lat1)
    dlon = np.radians(lon2 - lon1)

    a = (np.sin(dlat / 2) * np.sin(dlat / 2) +
         np.cos(np.radians(lat1)) * np.cos(np.radians(lat2)) *
         np.sin(dlon / 2) * np.sin(dlon / 2))

    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    distance = r * c
    return distance


# Ler arquivo json usando codificação 'utf-8'
with open("pedidos.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Carregar os dados do JSON (assumindo que já estão carregados na variável `data`)
estabelecimento_id = data["id"]
pedidos = data["entregas"]

# Criar uma instância da árvore AVL
avl_tree = AVLTree()

# Inserir os pedidos na árvore AVL
for pedido in pedidos:
    pedido_obj = Pedido(pedido)
    chave = (estabelecimento_id, pedido_obj.id)  # Chave é uma tupla (estabelecimento_id, pedido_id)
    avl_tree.insert(chave, pedido_obj)  # Supondo que insert possa aceitar uma chave e um valor



print("Travessia em ordem da árvore AVL:")
avl_tree.in_order_traversal()

print("\nBusca por chave:")
avl_tree.search((1, 2))  # Busca pelo pedido com chave (1, 2) / buscar o pedido com estabelecimento_id = 1 e pedido_id = 2, por exemplo

# Criar matriz localização
locations = [data['localizacao']]
destinatarios = ["McDonalds"]  # Lista para armazenar os destinatários, começando com o nome do estabelecimento
for entrega in data['entregas']:
    locations.append(entrega['localizacao'])
    destinatarios.append(entrega['destinatario'])

# Calcula matriz de distâncias usando Haversine
num_locations = len(locations)
distance_matrix = np.zeros((num_locations, num_locations))
for i in range(num_locations):
    for j in range(num_locations):
        distance_matrix[i, j] = haversine_distance(locations[i], locations[j])

permutation, distance = solve_tsp_dynamic_programming(distance_matrix)

# Exibindo a melhor rota usando o campo "destinatario"
print("Melhor rota:")
route = " -> ".join([destinatarios[i] for i in permutation]) + " -> " + destinatarios[
    0]  # Adicionando o nome do estabelecimento ao final
print(route)

# Informando a distância total
print("\nDistância total da rota: {:.2f} km".format(distance))
