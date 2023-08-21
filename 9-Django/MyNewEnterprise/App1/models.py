# App1/models.py
from django.db import models

class Cliente(models.Model): # Esto indica que la clase Cliente es un modelo que interactuará con la base de datos
    # id se crea automáticamente
    nombre = models.CharField(max_length=50)
    ruc = models.IntegerField()
    dv = models.IntegerField()

class Cuentas(models.Model):
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE) # Llave foránea a clientes
    n_cuenta = models.IntegerField()
    saldo = models.FloatField()
