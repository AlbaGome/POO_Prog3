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
        
    def puede_retirar(self, valor_a_retirar):
        valor_disponible_para_retirar = self._saldo + self._limite
        return valor_a_retirar <= valor_disponible_para_retirar

    def retirar(self, valor):
        if (self.puede_retirar(valor)):
            self.__saldo -= valor
        else:
            print('El valor {} pasó el límite'.format(valor))
  
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
        
    @staticmethod
    def codigo_banco():
        return "001"