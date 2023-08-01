from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def signup(request):
       if request.method == 'POST':
           form = UserCreationForm(request.POST)
           if form.is_valid():
               form.save()
               # Redirigir al usuario a una página de éxito o cualquier otra página deseada.
       else:
           form = UserCreationForm()
       return render(request, 'accounts/signup.html', {'form': form})
