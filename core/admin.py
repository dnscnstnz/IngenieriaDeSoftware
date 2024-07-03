from django.contrib import admin
from .models import Empresa,CategoriaVehiculo, Vehiculo, Reserva

# Register your models here.

admin.site.register(Empresa)
admin.site.register(CategoriaVehiculo)
admin.site.register(Vehiculo)
admin.site.register(Reserva)