#o .copy cria outro oobjeto com os mesmos dados, porém sendo outro objeto.
lista = [1, 3 ,5 ,6 ,7]
l2 = lista.copy()
l2[0] = 2

print(l2)
print(lista)