# ESCOPO GLOBAL: consegue pegar uma variavel das raiz do programa. Como no exemplo a seguir:
# o codigo comentado mostra que como lista é mutavel, tem que criar uma copia, caso queira fazer uma alteração no valor sem mudar o valor original.

salario = 2000

def salario_bonus(bonus): 
    global salario
    
    # lista_auxiliar = lista.copy()
    # lista_auxiliar.append(2)
    # print(f"lista auxiliar = {lista_auxiliar} ")

    salario += bonus
    return salario


# lista = [1]
salario_com_bonus = salario_bonus(800)

print(salario_com_bonus)
# print(lista)