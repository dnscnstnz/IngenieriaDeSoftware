from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Empresa, Vehiculo
from django.contrib.auth import logout, authenticate, login
from .forms import VehiculoForm,RealizarReserva
import datetime


def index(request):
    return render(request, 'index.html')

def empresas(request):
    empresas = Empresa.objects.all()
    context = {'empresas': empresas}
    return render(request, 'empresa_detail.html', context)

def reservar(request):
    return render(request, 'reservar.html')


def empresa_detail(request):
    empresas = Empresa.objects.all()
    context = {'empresas': empresas}
    return render(request, 'empresa_detail.html', context)

def adminTransfer(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'adminTransfer.html', {'vehiculos':vehiculos})

def cerrar(request):
    logout(request)
    return redirect('index')

def crear(request):
    if request.method=='POST':
        vehiculoform = VehiculoForm(request.POST, request.FILES)
        if vehiculoform.is_valid():
            vehiculoform.save()         
            return redirect ('adminTransfer')
    else:
        vehiculoform=VehiculoForm()
    return render(request, 'crear.html',{'vehiculoform':vehiculoform})

def modificar(request, id):
    vehiculo = Vehiculo.objects.get(idVehiculo=id)
    datos={
        'forModificar': VehiculoForm(instance=vehiculo), 
        'vehiculo': vehiculo
    }
    if request.method=='POST':
        formulario=VehiculoForm(request.POST, request.FILES, instance=vehiculo)
        if formulario.is_valid():
            formulario.save()           
            return redirect('adminTransfer')
    return render(request, 'modificar.html', datos)

def eliminar(request, id):
    vehiculo = get_object_or_404(Vehiculo, idVehiculo=id)
    if request.method=='POST':
        if 'eliminar' in request.POST:       
            vehiculo.delete()               
            return redirect ('adminTransfer')
        else:
            return redirect('detalle', idVehiculo=id)
    return render(request, 'eliminar.html', {'vehiculo': vehiculo})

def crearReserva(request):
    if request.method == 'POST':
        formReserva = RealizarReserva(request.POST)
        if formReserva.is_valid():
            reserva = formReserva.save(commit=False)
            reserva.fechaReserva = datetime.datetime.now()

            
            vehiculos_disponibles = Vehiculo.objects.filter(disponibilidad=True)
            if vehiculos_disponibles.exists():
                reserva.idVehiculo = vehiculos_disponibles.first()
                reserva.total = reserva.idVehiculo.precioPorPersona * reserva.cantidadPasajero


                empresa = Empresa.objects.first()  
                if empresa is None:
                    return HttpResponse("No hay empresas disponibles.")
                reserva.idEmpresa = empresa

                
                reserva.save()

                vehiculo_asignado = reserva.idVehiculo
                vehiculo_asignado.disponibilidad = False
                vehiculo_asignado.save()

                return redirect('index')
            else:
                return HttpResponse("Lo sentimos, no hay vehículos disponibles en este momento.")
    else:
        formReserva = RealizarReserva()

    vehiculos_disponibles = Vehiculo.objects.filter(disponibilidad=True)
    context = {
        'formReserva': formReserva,
        'vehiculos_disponibles': vehiculos_disponibles,
    }
    return render(request, 'reservar.html', context)


def consultar_disponibilidad(request):
    if request.method == 'GET':
        disponibilidad = request.GET.get('disponibilidad')

        if disponibilidad in ['True', 'False']:
            disponibilidad_bool = True if disponibilidad == 'True' else False
            vehiculos = Vehiculo.objects.filter(disponibilidad=disponibilidad_bool)
        else:
            vehiculos = Vehiculo.objects.all()  

        context = {
            'vehiculos': vehiculos
        }
        return render(request, 'consultarDispo.html', context)

    return render(request, 'consultarDispo.html', {'vehiculos': []})