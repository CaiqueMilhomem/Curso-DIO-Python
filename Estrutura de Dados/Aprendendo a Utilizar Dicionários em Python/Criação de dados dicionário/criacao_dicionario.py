dados_caique = {"Nome" : "Caique Ferreira Milhomem", "Idade" : "19"}

dados_caique2 = dict(nome="Caique Ferreira Milhomem", idade="19")

dados_caique2["telefone"] = "(11)96849-0591"

# ACESSAR VALOR DO DICIONÁRIO: 

print(dados_caique2["nome"])
print(dados_caique["Idade"])





# SOBRESCREVER VALOR DO DICIONÁRIO:

dados_caique2["idade"] = 20
print(dados_caique2)


####################################################################################################333

contatos = {
    "caique@gmail.com" : {"nome" : "Caique", "telefone" : "1234-5678"},
    "lituania@gmail.com" : {"nome" : "Lituania", "telefone" : "1234-5678"},
    "macedonia@gmail.com" : {"nome" : "Macedonia", "telefone" : "1234-5678"},
}

telefone_caique = contatos["caique@gmail.com"]["telefone"]

print(telefone_caique)


#utilizando for

for chave in contatos: 
    print(chave, contatos[chave])


for chave, valor in contatos.items():
    print(chave, valor)
