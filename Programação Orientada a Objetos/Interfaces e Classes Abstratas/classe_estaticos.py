class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def idade_com_data_nascimento(cls, dia, mes, ano, nome):
        idade = 2024 - ano
        return cls(nome, idade)
    
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18

    
# p = Pessoa("Caique", 20)
# print(p.nome, p.idade)
p2 = Pessoa.idade_com_data_nascimento(7, 6, 2004, "Caique")
print(p2.nome, p2.idade)
print(Pessoa.e_maior_idade(19))
print(Pessoa.e_maior_idade(9))
