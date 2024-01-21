nome = "GuiLhERme"

# maiuscula
print(nome.upper())

#minuscula
print(nome.lower())

# primeira letra maiuscula e segunda minuscula
print(nome.title())


#########################################################################################


texto = "   Olá, mundo!    "

#corta os espaços do inicio e do fim (da esquerda e da direita). 
print(texto.strip() + ".")

#corta os espaços da esquerda.
print(texto.lstrip() + ".")

#corta os espaços da direita.
print(texto.rstrip() + ".")


#########################################################################################


menu = "Python"


# centraliza e pode adicionar algum caracter. 
print ("####" + menu + "####")
print(menu.center(14, "#"))
print(menu.center(14))



print("-".join(menu))

