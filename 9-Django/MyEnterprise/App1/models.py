# App1/models.py
from django.db import models

class Cliente(models.Model):
    # id se crea automáticamente
    nombre = models.CharField(max_length=50)
    run = models.IntegerField()
    dv = models.IntegerField()

class Cuentas(models.Model):
    # El id de cuentas también se crea de manera automática
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE) # Llave foránea a clientes
    n_cuenta = models.IntegerField()
    saldo = models.FloatField()