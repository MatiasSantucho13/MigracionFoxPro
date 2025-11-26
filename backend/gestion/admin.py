from django.contrib import admin
from .models import Cliente  # <--- Importante: esto trae tu tabla

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'cuit', 'localidad', 'provincia')
    search_fields = ('nombre', 'cuit')