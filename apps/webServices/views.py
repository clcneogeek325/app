from django.shortcuts import HttpResponse
from apps.producto.models import producto
from django.core import serializers

def wsProductos(request):
	lista_de_productos = producto.objects.all()
	datos = serializers.serialize('json',lista_de_productos)
	return HttpResponse(datos,mimetype='application/json')
