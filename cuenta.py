class Cuenta:
    def __init__(self,numero, titular,saldo,limite):
        print("Construyendo el objeto...{}".format(self))
        self._numero =numero
        self._titular =titular
        self._saldo=saldo
        self._limite=limite 
        
    def extracto(self):
        print('saldo {} del titular {}'.format (self._saldo,self._titular))
        
        
    def depositar (self,valor):
        self._saldo += valor
        
         
    def retirar(self, valor):
        self._saldo -= valor
        
    def transferir(self, valor, destino):
        self.retirar(valor)
        destino.depositar(valor)
        
    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite    