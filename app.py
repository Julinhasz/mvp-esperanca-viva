class EstoqueComunitario:
    def __init__(self):
        self.itens = {}

    def adicionar_doacao(self, item: str, quantidade: int):
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")
        item_normalizado = item.strip().lower()
        self.itens[item_normalizado] = self.itens.get(item_normalizado, 0) + quantidade
        return self.itens[item_normalizado]

    def registrar_saida(self, item: str, quantidade: int):
        item_normalizado = item.strip().lower()
        if item_normalizado not in self.itens:
            raise KeyError("Item não encontrado no estoque.")
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")
        if quantidade > self.itens[item_normalizado]:
            raise ValueError("Estoque insuficiente para distribuição.")
        
        self.itens[item_normalizado] -= quantidade
        return self.itens[item_normalizado]

    def consultar_saldo(self, item: str):
        return self.itens.get(item.strip().lower(), 0)

    def relatorio_geral(self):
        return dict(self.itens)


if __name__ == "__main__":
    sistema = EstoqueComunitario()
    print("=== Associação Comunitária Esperança Viva ===")
    sistema.adicionar_doacao("Arroz (kg)", 50)
    sistema.adicionar_doacao("Feijão (kg)", 30)
    print("Estoque atualizado:", sistema.relatorio_geral())


# Validação e controle de itens atualizados para a comunidade
