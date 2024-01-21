#usando apenas o if

MAIOR_IDADE = 18
IDADE_ESPECIAL = 17


idade = int(input("Informe sua idade:"))

if idade >= MAIOR_IDADE:
    print("Você pode tirar a CNH.")

if idade < MAIOR_IDADE:
    print("Você não pode tirar a CNH, por ter menos de 18 anos!")

#usando if e else

if idade >= MAIOR_IDADE:
    print("Você pode tirar a CNH.")

else:
    print("Você não pode tirar a CNH, por ter menos de 18 anos!")

#usando if else e elif

if idade >= MAIOR_IDADE:
    print("Você pode tirar sua CNH!")

elif idade == IDADE_ESPECIAL:
    print("Você pode fazer as aulas teoricas")

else:
    print("Você não pode tirar sua CNH e para fazer as aulas teóricas precisa fazer pelos menos 16 anos. ")

