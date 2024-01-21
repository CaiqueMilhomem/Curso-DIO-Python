#.sort vai oredenar a lista, sendo em ordem crescente, revertendo, alfabetica, entre outros.

cores = ["Amarelo","Vermelho","Vermelho","Verde","Amarelo","Cinza","Cinza","Cinza","Amarelo"]

cores.sort(reverse=True)
print(cores)

cores.sort(key=lambda x: len(x))
print(cores)

cores.sort(key=lambda x: len(x), reverse=True)
print(cores)