from django.urls import path
from . import views
from .views import registro_gym_view
urlpatterns = [
    path('', views.index , name='index'),
    path('home/', views.index , name='home'),
    path('about/', views.about , name='about'),
    path('class/', views.clases , name='clases'),
    path('contact/', views.contact , name='contact'),
    path('blog/', views.blog , name='blog'),
    path('single/', views.single , name='single'),
    path('feature/', views.feature , name='feature'),
    path('registro_gym/', registro_gym_view, name='registro_gym'),
    path('registro_exitoso/', views.registro_exitoso, name='registro_exitoso'),
]