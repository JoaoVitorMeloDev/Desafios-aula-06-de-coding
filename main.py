from services.estoque import executar_rota

print(executar_rota("/produtos", "POST", {"nome": "Camiseta", "quantidade": 1}))

print(executar_rota("/produtos", "GET"))

print(executar_rota("/produtos/buscar", "GET", {"nome": "Camiseta"}))

print(executar_rota("/produtos/atualizar", "PUT", {"nome": "Camiseta", "quantidade": 2}))

print(executar_rota("/produtos", "GET"))

print(executar_rota("/produtos/deletar", "DELETE", {"nome": "Camiseta"}))

print(executar_rota("/produtos", "GET"))

