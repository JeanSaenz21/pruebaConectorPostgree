from django.http import HttpResponse
from django.shortcuts import render

from pruebaConectividad.models import Bitacora,Empleados


def mostrarDatos(request):
    if request.GET.get('Id'):
        id_bitacora = request.GET.get('Id')
        bitacoras = Bitacora.objects.filter(id_bitacora__icontains=int(id_bitacora))
        return render(request, "mostrarDatos.html", {"bitacoras": bitacoras, "query": id_bitacora})
    else:
        mensaje="No has introducido datos"
    return render(request, "mostrarDatos.html")


def mostrarDatosEmpleado(request):
    if request.GET.get('Id_empleado'):
        id_empleado = request.GET.get('Id_empleado')
        empleados = Empleados.objects.filter(id_empleado__icontains=int(id_empleado))
        return render(request, "mostrarDatosEmpleados.html", {"empleados": empleados, "query": id_empleado})
    else:
        mensaje="No has introducido datos"
    return render(request, "mostrarDatosEmpleados.html")