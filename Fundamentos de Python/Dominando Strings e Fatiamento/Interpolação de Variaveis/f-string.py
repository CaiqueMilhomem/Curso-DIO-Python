nome = "Caique"
idade = 19
profissao = "Programador"
curso = "Python"
QI = 135.5674

print(f"Olá, meu nome é {nome}. Tenho {idade} anos e trabalho como {profissao}. No momento estou fazendo um curso de {curso} e meu Qi é de {QI: .3f}.")

dados = {"nome": "Caique", "idade": 19}

print("Nome: {} Idade: {}".format(nome, idade))
print("Nome: {0} Idade: {1}".format(nome, idade))
print("Nome: {name} Idade: {age}".format(age = idade, name = nome ))
print("Nome: %s Idade: %d " % (nome, idade))
print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Meu nome é {nome}, tenho {idade} anos e meu QI é de {QI: .2f}")
print(f"Meu nome é {nome}, tenho {idade} anos e meu QI é de {QI: 10.2f}")
