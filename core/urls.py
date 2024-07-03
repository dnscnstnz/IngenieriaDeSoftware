from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('empresas/', views.empresas, name='empresas'),
    path('reservar/', views.crearReserva, name='reservar'),
    path('empresa_detail/', views.empresa_detail, name='empresa_detail'),
    path('adminTransfer/', views.adminTransfer, name='adminTransfer'),
    path('cerrar/', views.cerrar, name='cerrar'),
    path('crear/', views.crear, name='crear'),
    path('modificar/<int:id>/', views.modificar, name='modificar'),
    path('eliminar/<int:id>/', views.eliminar, name='eliminar'),
    path('consultaDispo/',views.consultar_disponibilidad, name="ConsultaDispo")
]

