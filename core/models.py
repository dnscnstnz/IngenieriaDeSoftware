from django.db import models
import datetime

class Empresa(models.Model):
    idEmpresa = models.IntegerField(primary_key=True, verbose_name='Id Empresa')
    nombre = models.CharField(max_length=50, verbose_name='Nombre Empresa')
    logo = models.ImageField(upload_to="imagenes", null=True, verbose_name='Logo')
    cantVan = models.IntegerField(null=True, verbose_name='Cantidad de Vans')
    cantAutos = models.IntegerField(null=True,verbose_name='Cantidad de Automoviles')
    cantBuses = models.IntegerField(null=True, verbose_name='Cantidad de Buses')

    def __str__(self):
        return self.nombre

class CategoriaVehiculo(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id Categoría')
    nombreCategoria = models.CharField(max_length=40, verbose_name='Nombre Categoría')

    def __str__(self):
        return self.nombreCategoria

class Vehiculo(models.Model):
    idEmpresa = models.ForeignKey('Empresa', on_delete=models.CASCADE, verbose_name='Id Empresa', related_name='vehiculos')
    idCategoria = models.ForeignKey('CategoriaVehiculo', on_delete=models.CASCADE, verbose_name='Id Categoría')
    idVehiculo = models.CharField(primary_key=True, max_length=5, verbose_name='Id Vehículo')
    patente = models.CharField(max_length=6, unique=True, default='ABCD00', verbose_name='Patente Vehículo')  
    cantPasajeros = models.IntegerField(verbose_name='Capacidad del Vehículo')
    descripcion = models.CharField(max_length=255, verbose_name='Descripción')
    imagen = models.ImageField(upload_to='vehiculos/', null=True, verbose_name='Imagen')
    marca = models.CharField(max_length=50, verbose_name='Marca Vehículo')
    precioPorPersona = models.IntegerField(verbose_name='Valor por Persona')
    disponibilidad= models.BooleanField(default=True,verbose_name="Disponibilidad Transfer")

    def __str__(self):
        return self.idVehiculo

class Reserva(models.Model):
    idReserva = models.CharField(primary_key=True, verbose_name='Pasaporte Cliente',default=1,max_length=50)
    idVehiculo = models.ForeignKey('Vehiculo', on_delete=models.CASCADE, verbose_name='Id Vehículo', related_name='reservas')
    idEmpresa = models.ForeignKey('Empresa', on_delete=models.CASCADE, verbose_name='Id Empresa', related_name='reservas')
    total = models.BigIntegerField(verbose_name='Total')
    fechaReserva = models.DateTimeField(blank=False, null=False, default=datetime.datetime.now, verbose_name='Fecha de Reserva')
    estado = models.CharField(max_length=50, default="Vehículo Reservado", verbose_name='Estado') 
    disponibilidad = models.BooleanField(default=True,max_length=10,verbose_name="Disponibilidad Transfer")
    nombre= models.CharField(max_length=50,verbose_name="Nombre",default="nombre por defecto")
    apellido= models.CharField(verbose_name="Apellido",max_length=50,default="Apellido por defecto")
    cantidadPasajero = models.IntegerField(verbose_name="Cantidad de pasajero",default=1)
    destino =models.CharField(verbose_name="Destino", max_length=60,default="destino por defecto")

    def __str__(self):
        return str(self.idReserva)
