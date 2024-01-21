# modo errado de fazer a repetição. 
# O FOR  é utilizado quando sabe o número correto de vez que quer percorrer o código
a = int(input("Informe um número:"))
print(a)

a = a + 1
print(a)

print(a)

# utilizando o for

texto = "Caique"
VOGAIS = "AEIOU"
for letra in texto: 
    if letra.upper() in VOGAIS:
        print(letra)


#utilizando range e fazendo uma tabuada com o mesmo. 

for numero in range(0, 11):
    print(numero)

for numero in range(0, 51, 5):
    print(numero)