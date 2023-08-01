from django.contrib import admin
from .models import GymMember

@admin.register(GymMember)
class GymMemberAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email')
    list_filter = ('nombre',)
    search_fields = ('nombre', 'email')

    fieldsets = (
        ('Información Personal', {
            'fields': ('nombre', 'email')
        }),
        ('Contraseña', {
            'fields': ('password',),
            'classes': ('collapse',),
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('password',)
        return self.readonly_fields
