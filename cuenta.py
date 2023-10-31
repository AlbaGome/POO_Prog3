class Cuenta:
    def __int__(self,numero,titular,saldo,limite):
        print("Construyendo el objeto...{}".format(self))
        self.numero = numero
        self.titular= titular
        self.saldo =saldo
        self.limite = limite