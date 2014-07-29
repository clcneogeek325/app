from django.db import models

class producto(models.Model):
	nombre  = models.CharField(max_length=50)
	stock = models.IntegerField(max_length=5)
	precio_compra = models.FloatField() 
	precio_venta =  models.FloatField() 
        email = models.EmailField()
	comentario = models.TextField(max_length=200)
	fecha_ingreso = models.DateTimeField()
	caducidad = models.DateField()
	hora = models.TimeField()
	status  = models.BooleanField(default=True)
	def __unicode__(self):
		return self.nombre



