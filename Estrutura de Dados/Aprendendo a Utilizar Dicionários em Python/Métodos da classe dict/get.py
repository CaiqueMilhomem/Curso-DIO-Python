# get serve como se fosse uma busca. 

contato = {
    "Caique" : {"telefone" : "(1196849-0591)", "email" : "caique@124.com"}
    }

print(contato.get("Caique"))
print(contato.get("link", {}))
#caso busqye uyma chave inexistente irá printarcomo "none".
