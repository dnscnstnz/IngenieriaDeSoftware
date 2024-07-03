from django import forms 
from .models import CategoriaVehiculo, Vehiculo,Reserva
from django.forms import ModelForm
from django.forms import widgets
from django.forms.widgets import Widget




class RealizarReserva(forms.ModelForm):
    class Meta:
        model=Reserva
        fields =['nombre','apellido','idReserva','cantidadPasajero','destino']
        labels ={
            'nombre':'Nombre',
            'apellido':'Apellido',
            'idReserva':'Numero Pasaporte',
            'cantidadPasajero':'Cantidad de Pasajeros',
            'destino':'Destino',
        }
        widgets={
            'nombre': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su nombre',
                    'id':'nombre'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su apellido',
                    'id':'apellido'
                }
            ),
            'idReserva': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su Pasaporte',
                    'id':'idReserva'
                }
            ),
            'cantidadPasajero': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese la cantidad de pasajeros',
                    'id':'cantidadPasajero'
                }
            ),
            'destino': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su destino',
                    'id':'destino'
                }
            ),
        }

class VehiculoForm(forms.ModelForm):
    class Meta: 
        model = Vehiculo
        fields = ['idVehiculo', 'idEmpresa', 'idCategoria', 'patente', 'cantPasajeros','descripcion','imagen','marca','precioPorPersona','disponibilidad']
        labels = {
            'idVehiculo': 'ID Vehiculo',
            'idEmpresa': 'ID Empresa',
            'idCategoria': 'ID Categoria',
            'patente': 'Patente',
            'cantPasajeros': 'Capacidad',
            'descripcion': 'Descripción',
            'imagen' : 'Imagen',
            'marca' : 'Marca',
            'precioPorPersona': 'Valor por Persona',
            'disponibilidad':'Disponibilidad Transfer'
        }
        widgets ={
            'idVehiculo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Id Vehiculo',
                    'id': 'idvehiculo'
                }
            ),
            'idEmpresa': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese ID Empresa',
                    'id': 'idEmpresa'
                }
            ),
            'idCategoria': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese ID Categoria',
                    'id': 'idCategoria'
                }
            ),
            'patente': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese patente del Vehiculo',
                    'id': 'patente'
                }
            ),
            'cantPasajeros': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese capacidad del vehiculo',
                    'id': 'cantPasajeros'
                }
            ),
            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese descripcion del Vehiculo',
                    'id': 'descripcion'
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese precio Vehiculo',
                    'id': 'precio'
                }
            ),
            'marca': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese marca Vehiculo',
                    'id': 'marca'
                }
            ),
            'precioPorPersona': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese valor por persona',
                    'id': 'precioPorPersona'
                }
            ),
            'disponibilidad': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la disponibilidad del transfer',
                    'id': 'disponibilidad'
                }
            ),
            
        }
