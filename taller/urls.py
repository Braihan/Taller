from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('singup/', views.singup, name='singup'),
    path('tareas/', views.tareasenespera, name='tareas'),
    path('tareascompletadas/', views.tareascompletadas, name='tareascompletadas'),
    path('tareas/creartarea/', views.creartarea, name='creartarea'),
    path('tareas/<int:tarea_id>/', views.detalletarea, name='detalletarea'),
    path('tareas/<int:tarea_id>/tareaenproceso/', views.tareaenproceso, name='tareaenproceso'),
    path('tareas/<int:tarea_id>/borrartarea/', views.borrartarea, name='borrartarea'),
    path('tareas/clientenuevo/', views.crearcliente, name='crearcliente'),
    path('tareas/cargarstock/', views.crearstock, name='crearstock'),
    path('tareas/listastock/', views.listadostock, name='listastock'),
    path('tareas/detallestock/<int:stock_id>/', views.detallestock, name='detallestock'),
    path('tareas/<int:stock_id>/borrarstock/', views.borrarstock, name='borrarstock'),
    path('Logout/', views.signout, name='logout'),
    path('singin/', views.singin, name='singin'),
    path('tareas/listadeclientes/', views.listadecliente, name='listadeclientes'),
    path('tareas/<int:cliente_id>/borrarcliente/', views.borrarcliente, name='borrarcliente'),
    path('tareas/detallecliente/<int:cliente_id>/', views.detallecliente, name='detallecliente'),
    
              
]
