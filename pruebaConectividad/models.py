from django.db import models


class Bitacora(models.Model):
    id_bitacora = models.IntegerField(primary_key=True)
    tabla_afectada = models.CharField(max_length=60)
    operacion = models.CharField(max_length=10)
    usuario = models.CharField(max_length=15)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    consulta_realizada = models.TextField()

    class Meta:
        db_table = 'bitacora'

class Empleados(models.Model):
    id_empleado = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=60)
    apellido_mat = models.CharField(max_length=60)
    apellido_pat = models.CharField(max_length=60)
    calle = models.CharField(max_length=60)
    num_calle = models.CharField(max_length=4)
    cod_postal = models.CharField(max_length=5)
    nss = models.CharField(max_length=20)
    curp = models.CharField(max_length=18)
    rfc = models.CharField(max_length=13)
    fecha_nac = models.DateField()
    fecha_ingreso = models.DateField()

    class Meta:
        db_table = 'empleados'