class Cuenta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construyendo el objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        
    def extracto(self):
        print('Saldo {} del titular {}'.format(self._saldo, self._titular))
        
    def depositar(self, valor):
        self.__saldo += valor
        
    def retirar(self, valor):
        self.__saldo -= valor
        
    def transferir(self, valor, destino):
        self.retirar(valor)
        destino.depositar(valor)
        
    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite