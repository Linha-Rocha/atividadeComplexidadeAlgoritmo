import json
from typing import List, Tuple

# Definindo a estrutura de um Pedido
Pedido = Tuple[float, float]  # (peso, valor de entrega)


def extrair_pedidos_de_arquivo(arquivo_json: str) -> List[Pedido]:
    """
    Extrai os pedidos do arquivo JSON fornecido.

    :param arquivo_json: Caminho do arquivo JSON.
    :return: Lista de pedidos extraídos do arquivo JSON.
    """
    with open(arquivo_json, 'r', encoding='utf-8') as file:
        dados = json.load(file)

    pedidos = []
    for entrega in dados.get("entregas", []):
        peso = entrega.get("peso", 0)
        valor_entrega = entrega.get("total_entrega", 0)
        pedidos.append((peso, valor_entrega))

    return pedidos


def otimizador_mochila(pedidos: List[Pedido], carga_total: float) -> List[Pedido]:
    """
    Implementa o otimizador de mochila para maximizar o valor de entrega dos pedidos,
    respeitando a carga máxima da mochila.

    :param pedidos: Lista de pedidos, onde cada pedido é uma tupla (peso, valor de entrega).
    :param carga_total: Capacidade máxima de peso da mochila.
    :return: Lista de pedidos selecionados para otimização.
    """
    # Ordenar os pedidos primeiro pelo peso (crescente) e depois pelo valor (decrescente)
    pedidos_ordenados = sorted(pedidos, key=lambda x: (x[0], -x[1]))

    peso_atual = 0.0
    mochila = []

    for pedido in pedidos_ordenados:
        peso_pedido, valor_pedido = pedido
        if peso_atual + peso_pedido <= carga_total:
            mochila.append(pedido)
            peso_atual += peso_pedido

    return mochila
