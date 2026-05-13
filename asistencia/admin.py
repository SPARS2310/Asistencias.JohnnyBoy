from django.contrib import admin
from .models import Empleado, Registro

# ============================================================
# Personalización del sitio de administración
# Johnny Boy Barber Shop
# ============================================================
admin.site.site_header = "Johnny Boy Barber Shop"
admin.site.site_title = "Johnny Boy - Admin"
admin.site.index_title = "Panel de Administración"


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'uid_rfid', 'total_registros')
    search_fields = ('nombre', 'uid_rfid')
    list_per_page = 20
    ordering = ('nombre',)

    fieldsets = (
        ('Información del Barbero', {
            'fields': ('nombre', 'uid_rfid'),
            'description': 'Datos del empleado y su tarjeta RFID asignada.'
        }),
    )

    def total_registros(self, obj):
        return obj.registro_set.count()
    total_registros.short_description = 'Total de Registros'


@admin.register(Registro)
class RegistroAdmin(admin.ModelAdmin):
    list_display = ('empleado', 'tipo', 'fecha_hora')
    list_filter = ('tipo', 'fecha_hora', 'empleado')
    search_fields = ('empleado__nombre', 'empleado__uid_rfid')
    date_hierarchy = 'fecha_hora'
    list_per_page = 30
    ordering = ('-fecha_hora',)
    readonly_fields = ('fecha_hora',)

    fieldsets = (
        ('Detalles del Registro', {
            'fields': ('empleado', 'tipo', 'fecha_hora'),
        }),
    )