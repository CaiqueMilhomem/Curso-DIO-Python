# serve quando você quer adicionar um valor no dicionário, porém só caso ele não exista. 

contatos = {"nome" : "Caique", "idade" : "19"}

contatos.setdefault("idade", "29")
print(contatos)

contatos.setdefault("sexo", "masculino")
print(contatos)