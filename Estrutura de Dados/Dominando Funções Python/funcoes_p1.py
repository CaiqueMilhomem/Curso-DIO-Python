def exibir_mensagem1(): 
    print("Olá, mundo")

def exibir_mensagem2(nome): 
    print(f"Olá, {nome}")

def exibir_mensagem3(nome="Anônimo"): 
    print(f"Olá, {nome}")


exibir_mensagem1()
exibir_mensagem2(nome="Caique")
exibir_mensagem3()
exibir_mensagem3(nome="Gustavo")


