from django.contrib import admin
from .models import Empleado, Registro

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'uid_rfid')
    search_fields = ('nombre', 'uid_rfid')

@admin.register(Registro)
class RegistroAdmin(admin.ModelAdmin):
    list_display = ('empleado', 'tipo', 'fecha_hora')
    list_filter = ('tipo', 'fecha_hora')