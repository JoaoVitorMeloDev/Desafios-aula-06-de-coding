class Produtos:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

    def to_dict(self):
        return {
            'nome': self.nome,
            'quantidade': self.quantidade
        }