class Pedido:
    def __init__(self, pedido_data):
        self.id = pedido_data["id"]
        self.destinatario = pedido_data["destinatario"]
        self.endereco = pedido_data["endereco"]
        self.localizacao = pedido_data["localizacao"]
        self.produtos = pedido_data["produtos"]
        self.total_entrega = pedido_data["total_entrega"]
        self.total_desconto = pedido_data["total_desconto"]
        self.codigo_entrega = pedido_data["codigo_entrega"]
        self.pago = pedido_data["pago"]
        self.tipo_pagamento = pedido_data["tipo_pagamento"]

    def __str__(self):
        return f"Pedido ID: {self.id}, Destinatário: {self.destinatario}, Endereço: {self.endereco}, Total: {self.total_entrega}"
