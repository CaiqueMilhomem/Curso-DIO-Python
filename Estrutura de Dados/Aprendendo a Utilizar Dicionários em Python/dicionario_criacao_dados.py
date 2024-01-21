dados_caique = {"Nome" : "Caique Ferreira Milhomem", "Idade" : "19"}

dados_caique2 = dict(nome="Caique Ferreira Milhomem", idade="19")

dados_caique2["telefone"] = "(11)96849-0591"

# ACESSAR VALOR DO DICIONÁRIO: 

print(dados_caique2["nome"])
print(dados_caique["Idade"])





# SOBRESCREVER VALOR DO DICIONÁRIO:

dados_caique2["idade"] = 20
print(dados_caique2)