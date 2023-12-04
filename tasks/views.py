from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TareasForm, ClienteForm
from .models import Tareas, Cliente
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.p
def home(request):
    return render(request, 'home.html')


def singup(request):
    if request.method == 'GET':
        return render(request, 'singup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # registrar usuarios
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tareas')
            except IntegrityError:
                return render(request, 'singup.html', {
                    'form': UserCreationForm,
                    'error': 'Username already exist'
                })
        return render(request, 'singup.html', {
            'form': UserCreationForm,
            'error': 'Password do not match'
        })

@login_required
def tareasenespera(request):
    listadetareas = Tareas.objects.filter(completado__isnull=True).order_by('-completado')
    return render(request, 'tareas.html', {'Tareas': listadetareas})

@login_required
def tareascompletadas(request):
    tareacompletada = Tareas.objects.filter(completado__isnull=False)
    return render(request, 'tareascompletadas.html', {'Tareas': tareacompletada})

@login_required
def creartarea(request):
    if request.method == 'GET':
        return render(request, 'creartarea.html')
    else:
        try:
            form = TareasForm(request.POST)
            nueva_tarea = form.save(commit=False)
            nueva_tarea.save()
            return redirect('tareas')

        except:
            return render(request, 'creartarea.html', {
                'form': TareasForm,
                'error': 'Ingrese datos validos'
            })
            
@login_required
def detalletarea(request, tarea_id):
    if request.method == 'GET':
        tareas = get_object_or_404(Tareas, pk=tarea_id)
        formt = TareasForm(instance=tareas)
        return render(request, 'detallestarea.html', {'tareas': tareas, 'formt': formt})
    else:
        try:
            tareas = get_object_or_404(Tareas, pk=tarea_id)
            formt = TareasForm(request.POST, instance=tareas)
            formt.save()
            return redirect('tareas')
        except ValueError:
            return render(request, 'detallestarea.html', {'tareas': tareas, 'formt': formt, 'error': 'Error al actualizar la tarea'})
        
@login_required
def detalletareacliente(request):
    if request.method == 'GET':
        cliente = get_object_or_404(Cliente)
        formc = ClienteForm(instance=cliente)
        return render(request, 'detallestarea.html', {'cliente': cliente, 'formc': formc})
    else:
        try:
            
            cliente = get_object_or_404(Cliente)
            formc = ClienteForm(request.POST, instance=cliente)
            formc.save()
            return redirect('tareas')
        except ValueError:
            return render(request, 'detallestarea.html', {'cliente': cliente, 'formc': formc, 'error': 'Error al actualizar la tarea'})       

@login_required
def tareaenproceso(request, tarea_id):
    tareas = get_object_or_404(Tareas, pk=tarea_id)
    if request.method == 'POST':
        tareas.completado = timezone.now()
        tareas.save()
        return redirect('tareas')

@login_required
def borrartarea(request, tarea_id):
    tareas = get_object_or_404(Tareas, pk=tarea_id)
    if request.method == 'POST':
        tareas.delete()
        return redirect('tareas')
    

@login_required
def signout(request):
    logout(request)
    return redirect('home')


def singin(request):
    if request.method == 'GET':
        return render(request, 'singin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'singin.html', {
                'form': AuthenticationForm,
                'error': 'User or paswor is incorrect'
            })
        else:
            login(request, user)
            return redirect('tareas')
        
@login_required
def listadecliente(request):
    clientes = Cliente.objects.all()
    return render(request, 'listadeclientes.html', {'Cliente': clientes})

@login_required
def detallecliente(request, cliente_id):
    if request.method == 'GET':
        clientes = get_object_or_404(Cliente, pk=cliente_id)
        form = ClienteForm(instance=clientes)
        return render(request, 'detallecliente.html', {'clientes': clientes, 'form': form})
    else:
        try:
            clientes = get_object_or_404(Cliente, pk=cliente_id)
            form = ClienteForm(request.POST,instance=clientes)
            form.save()
            return redirect('listadeclientes')
        except ValueError:
            return render(request, 'detallecliente.html', {'clientes': clientes, 'form': form, 'error': 'Error al actualizar cliente'})

        
@login_required
def borrarcliente(request, cliente_id):
    clientes = get_object_or_404(Cliente, pk=cliente_id)
    if request.method == 'POST':
        clientes.delete()
        return redirect('listadeclientes')

@login_required
def crearcliente(request):
    if request.method == 'GET':
        return render(request, 'clientenuevo.html', {
            'form': ClienteForm
        })
    else:
        try:
            form = ClienteForm(request.POST)
            nuevo_cliente = form.save(commit=False)
            nuevo_cliente.save()
            return redirect('tareas')

        except:
            return render(request, 'clientenuevo.html', {
                'form': ClienteForm,
                'error': 'Error al registrar cliente'
            })