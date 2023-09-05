class Cuenta:
    def __init__(self, id, saldo=0):
        # Creamos los atributos de la cuenta
        # bancaria
        self.id = id
        self.saldo = saldo
        
    def showSaldo(self):
        # Este método solo muestra el saldo por pantalla
        print("El saldo de la cuenta", self.id, "es", self.saldo)
    
    def updateSaldo(self, newSaldo):
        # Actualizaremos el saldo dependiendo de la entrada
        # a este método
        self.saldo = newSaldo
        

class Banco:
    def __init__(self,cuentas=[]):
        self.cuentas = cuentas # Donde cuentas es una lista de las cuentas que tendrá mi banco

    def transferMoney(self, id_orig, id_dest, monto):
        # Primero debemos recorrer la lista de cuentas
        # para ver cuales de ellas son la de origen y la de destino
        # respectivamente
        for account in self.cuentas:
            if account.id == id_orig:
                cuenta_orig = account
                
            if account.id == id_dest:
                cuenta_dest = account
                
        if cuenta_orig.saldo >= monto:
            # Con esto sacamos el dinero de la cuenta
            cuenta_orig.updateSaldo(cuenta_orig.saldo - monto)
            # Agregamos el mismo monto en la cuenta de destino
            cuenta_dest.updateSaldo(cuenta_dest.saldo + monto)
            

# Creamos 3 cuentas
cuenta1 = Cuenta(1, 10000)
cuenta2 = Cuenta(2, 50000)
cuenta3 = Cuenta(3, 25000)

# Creamos la lista de cuentas
cuentas = [cuenta1, cuenta2, cuenta3]

# Creamos el banco con las cuentas
banco = Banco(cuentas)

# Y ahora transferimos entre dos cuentas
banco.transferMoney(2, 3, 10000)

# Vamos a revisar el saldo en todas las cuentas
for cuenta in cuentas:
    cuenta.showSaldo()