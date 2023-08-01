from django.urls import path
from .views import message_create_view, message_list_view

app_name = 'messages'

urlpatterns = [
    path('create/', message_create_view, name='create'),
    path('list/', message_list_view, name='list'),
]
