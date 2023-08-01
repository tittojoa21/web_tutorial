from django.contrib import admin
from .models import GymMember

@admin.register(GymMember)
class GymMemberAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email')
    list_filter = ('nombre',)
    search_fields = ('nombre', 'email')
