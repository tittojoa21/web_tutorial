from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import GymMember

class GymMembershipForm(UserCreationForm):
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()

    class Meta(UserCreationForm.Meta):
        model = GymMember
        fields = ('nombre', 'email', 'password1', 'password2')
