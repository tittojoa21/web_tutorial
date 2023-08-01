from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import GymMembershipForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def clases(request):
    return render(request, 'class.html')

def contact(request):
    return render(request, 'contact.html')

def feature(request):
    return render(request, 'feature.html')

def blog(request):
    return render(request, 'blog.html')

def single(request):
    return render(request, 'single.html')

def registro_gym_view(request):
    if request.method == 'POST':
        form = GymMembershipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registro_exitoso')  # Redirigir a la página de registro exitoso
    else:
        form = GymMembershipForm()
    return render(request, 'registro_gym.html', {'form': form})


def registro_exitoso(request):
    mensaje = "Registro exitoso"  # Puedes pasar datos adicionales a la plantilla
    return render(request, 'registro_exitoso.html', {'mensaje': mensaje})


class RegistroUsuarioView(CreateView):
    form_class = UserCreationForm
    template_name = 'registrados.html'
    success_url = reverse_lazy('index')  # Redirigir a la página principal después del registro exitoso
