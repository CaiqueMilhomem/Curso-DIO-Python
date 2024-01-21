#sorted() ordena itens iteraveis.

cores = ["Amarelo","Vermelho","Vermelho","Verde","Amarelo","Cinza","Cinza","Cinza","Amarelo"]



print(sorted(cores, key=lambda x: len(x)))