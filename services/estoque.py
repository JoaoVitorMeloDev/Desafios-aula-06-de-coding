from models.produtos import Produtos

def resposta(mensagem, status, dados=None):
    return {
        "mensagem": mensagem,
        "status": status,
        "dados": dados
    }

class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, nome, quantidade):
        if quantidade <= 0:
            return resposta("Quantidade inválida", "erro")
        
        for produto in self.produtos:
            if produto.nome.lower() == nome.lower():
                return resposta("Produto já existe", "erro")

        produto = Produtos(nome, quantidade)
        self.produtos.append(produto)

        return resposta("Produto adicionado com sucesso", "sucesso", produto.to_dict())
    
    def listar_produtos(self):
        lista = [produto.to_dict() for produto in self.produtos]
        return resposta("Produtos listados com sucesso", "sucesso", lista)

    def buscar_produto(self, nome):
        for produto in self.produtos:
            if produto.nome.lower() == nome.lower():
                return resposta("Produto encontrado", "sucesso", produto.to_dict())
        
        return resposta("Produto não encontrado", "erro")

    def atualizar_produto(self, nome, nova_quantidade):

        if nova_quantidade <= 0:
            return resposta("Quantidade inválida", "erro")

        for produto in self.produtos:
            if produto.nome.lower() == nome.lower():
                produto.quantidade = nova_quantidade
                return resposta("Quantidade atualizada", "sucesso", produto.to_dict())
        
        return resposta("Produto não encontrado", "erro")
    
    def remover_produto(self, nome):
        for produto in self.produtos:
            if produto.nome.lower() == nome.lower():
                self.produtos.remove(produto)
                return resposta("Produto removido", "sucesso")
        return resposta("Produto não encontrado", "erro")

estoque = Estoque()

def get_produtos():
    return estoque.listar_produtos()

def post_produto(nome, quantidade):
    return estoque.adicionar_produto(nome, quantidade)

def get_produto__por_nome(nome):
    return estoque.buscar_produto(nome)

def put_produto(nome, quantidade):
    return estoque.atualizar_produto(nome, quantidade)

def delete_produto(nome):
    return estoque.remover_produto(nome)

def executar_rota(rota, metodo, dados=None):
    if rota == "/produtos" and metodo == "GET":
        return get_produtos()
    
    if rota == "/produtos" and metodo == "POST":
        return post_produto(dados['nome'], dados['quantidade'])
    
    if rota == "/produtos/buscar" and metodo == "GET":
        return get_produto__por_nome(dados["nome"])
    
    if rota == "/produtos/atualizar" and metodo == "PUT":
        return put_produto(dados["nome"], dados['quantidade'])
    
    if rota == "/produtos/deletar" and metodo == "DELETE":
        return delete_produto(dados["nome"])
    else:
        return "Rota ou método não suportado."
