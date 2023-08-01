from django.contrib.auth.views import login

def login_view(request):
    return login(request, template_name='accounts/login.html')
