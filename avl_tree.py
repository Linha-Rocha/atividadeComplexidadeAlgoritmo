from node import Node


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        # Se a árvore estiver vazia, cria um novo nó e o define como raiz
        if self.root is None:
            self.root = Node(key, value)
        else:
            # Caso contrário, insere o nó de forma recursiva
            self.root = self._insert_recursive(self.root, key, value)

    def delete(self, root, key):
        # Passo 1: Executa a exclusão padrão de BST
        if not root:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # O nó a ser deletado foi encontrado
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # Nó com dois filhos: Obtém o sucessor (menor na subárvore direita)
            temp = self._getMinValueNode(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        # Se a árvore tem apenas um nó, retorna ele
        if root is None:
            return root

        # Passo 2: Atualiza a altura do nó atual
        root.height = 1 + max(self._getHeight(root.left),
                              self._getHeight(root.right))

        # Passo 3: Obtém o fator de balanceamento para verificar se o nó se tornou desbalanceado
        balance = self._getBalance(root)

        # Passo 4: Balanceamento

        # Caso A: Rotação simples à direita
        if balance > 1 and self._getBalance(root.left) >= 0:
            return self._rightRotate(root)

        # Caso B: Rotação esquerda-direita
        if balance > 1 and self._getBalance(root.left) < 0:
            root.left = self._leftRotate(root.left)
            return self._rightRotate(root)

        # Caso C: Rotação simples à esquerda
        if balance < -1 and self._getBalance(root.right) <= 0:
            return self._leftRotate(root)

        # Caso D: Rotação direita-esquerda
        if balance < -1 and self._getBalance(root.right) > 0:
            root.right = self._rightRotate(root.right)
            return self._leftRotate(root)

        return root

    def _getMinValueNode(self, node):
        if node is None or node.left is None:
            return node
        return self._getMinValueNode(node.left)

    def search(self, key):
        comparisons = 0
        result, comparisons = self._search_recursive(self.root, key, comparisons)
        if result:
            print(f"Valor encontrado: {result}")
        else:
            print("Valor não encontrado.")
        print(f"Total de comparações: {comparisons}")

    def _search_recursive(self, current_node, key, comparisons):
        if not current_node:
            return None, comparisons

        comparisons += 1
        if key == current_node.key:
            return current_node.value, comparisons
        elif key < current_node.key:
            return self._search_recursive(current_node.left, key, comparisons)
        else:
            return self._search_recursive(current_node.right, key, comparisons)

    def _rebalance(self, node):
        # Obter o fator de balanceamento
        balance = self._getBalance(node)

        # Se o nó está desbalanceado, há quatro casos:

        # Caso A: Rotação simples à direita
        if balance > 1 and self._getBalance(node.left) >= 0:
            return self._rightRotate(node)

        # Caso B: Rotação esquerda-direita
        if balance > 1 and self._getBalance(node.left) < 0:
            node.left = self._leftRotate(node.left)
            return self._rightRotate(node)

        # Caso C: Rotação simples à esquerda
        if balance < -1 and self._getBalance(node.right) <= 0:
            return self._leftRotate(node)

        # Caso D: Rotação direita-esquerda
        if balance < -1 and self._getBalance(node.right) > 0:
            node.right = self._rightRotate(node.right)
            return self._leftRotate(node)

        return node

    def _leftRotate(self, z):
        y = z.right  # Estabelece o nó direito de z como y
        T2 = y.left  # Subárvore esquerda de y se torna T2

        # Executa a rotação
        y.left = z
        z.right = T2

        # Atualiza as alturas
        z.height = 1 + max(self._getHeight(z.left), self._getHeight(z.right))
        y.height = 1 + max(self._getHeight(y.left), self._getHeight(y.right))

        # Retorna a nova raiz após rotação
        return y

    def _rightRotate(self, z):
        # Rotação à direita
        pass

    def _getHeight(self, node):
        if not node:
            return 0
        return node.height

    def _getBalance(self, node):
        if not node:
            return 0
        return self._getHeight(node.left) - self._getHeight(node.right)

    def _insert_recursive(self, current_node, key, value):
        if current_node is None:
            return Node(key, value)

        if key < current_node.key:
            current_node.left = self._insert_recursive(current_node.left, key, value)
        elif key > current_node.key:
            current_node.right = self._insert_recursive(current_node.right, key, value)
        else:
            # Chaves duplicadas não são permitidas na árvore AVL
            return current_node

        # Atualizar a altura do nó ancestral
        current_node.height = 1 + max(self._getHeight(current_node.left), self._getHeight(current_node.right))

        # Obter o fator de balanceamento
        balance = self._getBalance(current_node)

        # Se o nó estiver desbalanceado, há quatro casos

        # Rotação simples à direita
        if balance > 1 and key < current_node.left.key:
            return self._rightRotate(current_node)

        # Rotação à esquerda-direita
        if balance > 1 and key > current_node.left.key:
            current_node.left = self._leftRotate(current_node.left)
            return self._rightRotate(current_node)

        # Rotação simples à esquerda
        if balance < -1 and key > current_node.right.key:
            return self._leftRotate(current_node)

        # Rotação à direita-esquerda
        if balance < -1 and key < current_node.right.key:
            current_node.right = self._rightRotate(current_node.right)
            return self._leftRotate(current_node)

        return current_node

    def in_order_traversal(self):
        self._in_order_recursive(self.root)

    def _in_order_recursive(self, current_node):
        if current_node is not None:
            self._in_order_recursive(current_node.left)  # Visita a subárvore esquerda
            print(f"Chave: {current_node.key}, Valor: {current_node.value}")  # Visita o nó atual
            self._in_order_recursive(current_node.right)  # Visita a subárvore direita

