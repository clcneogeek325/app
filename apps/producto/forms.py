from django import forms
from apps.producto.models import producto



class productoForm(forms.ModelForm):
	class Meta:
		model = producto


