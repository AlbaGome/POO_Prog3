class Cliente:
    def __init__(self, nombre):
        self.__nombre = nombre
        
    @property
    def nombre(self):
        print('llamando a @property nombre()')
        return self.__nombre.title()
    
    @nombre.setter
    def nombre(self, nombre):
        print('llamando a setter nombre()')
        self.__nombre = nombre