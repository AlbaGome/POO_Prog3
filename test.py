def crear_cuenta(numero,titular,saldo,limite):
    cuenta = {'numero':numero, 'titular':titular,'saldo':saldo,'limite':limite}
    return cuenta
def depositar(cuenta, valor):
    cuenta['saldo'] = cuenta['saldo'] + valor
    
def retirar(cuenta,valor):
    cuenta['saldo'] = cuenta['saldo'] -valor
    
def extracto(cuenta):
    print('saldo actual es de Bs.{}'.format(cuenta['saldo']))
                            