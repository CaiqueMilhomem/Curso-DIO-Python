# serve para quando quer adicionar novas chaves no dicionário.

contato = dict.fromkeys(["nome", "telefone"])  # {"nome": None, "telefone": None}
print(contato)

contato = dict.fromkeys(["nome", "telefone"], "vazio")  # {"nome": "vazio", "telefone": "vazio"}
print(contato)


