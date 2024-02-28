class Conta: 
    def __init__(self, saldo=0):
        self._saldo = saldo

    def sacar(self, valor):
        self._saldo -= valor

    def depositar(self, valor):
        self._saldo += valor

    def mostrar_saldo(self):
        return self._saldo

conta = Conta(100)

conta.sacar(50)
conta.depositar(150)
print(conta.mostrar_saldo())