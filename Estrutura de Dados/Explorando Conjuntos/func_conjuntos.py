# .union faz a união

conjunto_a = {1, 2}
conjunto_b = {3, 4}

conjunto_a.union(conjunto_b) #  {1,2,3,4}



# .intersection mostra os itens iguais 

conjunto_c = {1, 2, 3}
conjunto_d = {2, 3, 4}

conjunto_c.intersection(conjunto_d) # {2,3}



# .diffference mostra a diferença de apenas 1 conjunto


conjunto_e = {1, 2, 3}
conjunto_f = {2, 3, 4}

conjunto_e.difference(conjunto_f) # {1}
conjunto_f.difference(conjunto_e) # {4}



# .symmetric_difference mostra a diferença de ambos conjuntos

conjunto_g = {1, 2, 3}
conjunto_h = {2, 3, 4}

conjunto_g.symmetric_difference(conjunto_h) # {1,4}



#.issubset ele mostra se uum conjunto é subconjunto de outro

conjunto_i = {1, 2, 3}
conjunto_j = {4, 1, 5, 2, 6, 3}

conjunto_i.issubset(conjunto_j) # False
conjunto_j.issubset(conjunto_i) # True



#isdisjoint true quando não há nenhum item identic

conjunto_k = {1, 2, 3}
conjunto_l = {4, 1, 5, 2, 6, 3}
conjunto_m = {9, 8, 7}

print(conjunto_k.isdisjoint(conjunto_l)) # False
print(conjunto_l.isdisjoint(conjunto_m)) # True



#.add serve para adicionar se ele não existe na lista

sorteio = {1, 27}

sorteio.add(37) # {1, 27, 37}
sorteio.add(39) # {1, 27, 37, 39}
sorteio.add(37) # {1, 27, 37, 39}



#.clear

sorteio2 = {2, 10}

sorteio2.clear()

sorteio2 # {}



#.copy 

sorteio3 = {2, 10}

sorteio2.copy()

sorteio3 # {2, 10}



#.discard discarta um valor

numeros1 = {4, 1, 5, 2, 6, 3}

numeros1.discard(4) # {1, 2, 3, 5, 6}




#.pop retira os valores da lista em ordem crescente, retira o valor da frente da lista

numeros2 = {4, 1, 5, 2, 6, 3, 7, 11}

numeros2.pop() # {2, 3, 4, 5, 6, 7, 11}





#.remove 

numeros2 = {4, 1, 5, 2, 6, 3, 7, 11}

numeros2.remove(1) # {2, 3, 4, 5, 6, 7, 11}




#len pega o tamonho do produto 

numeros3 = {2, 3, 4, 5, 6, 7, 11}

len(numeros3) #7




#in se um elemento está em um conjunto

numeros4 = {2, 3, 4, 5, 6, 7, 11}

2 in numeros4 # True
19 in numeros4 # False
