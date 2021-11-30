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

#def mostrarDatosBitacora(request):
#    if request.GET[""]:
