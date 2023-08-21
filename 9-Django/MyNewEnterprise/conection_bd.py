from App1.models import *

cliente1 = Cliente.objects.create(nombre="Damián", ruc=11111111, dv=1)

cuenta1_1 = Cuentas.objects.create(idCliente=cliente1, 
                    n_cuenta="153489", saldo=10000) # Creación de nueva cuenta
cuenta1_2 = Cuentas.objects.create(idCliente=cliente1,
                    n_cuenta="64895642", saldo=50000) # Cuenta adicional