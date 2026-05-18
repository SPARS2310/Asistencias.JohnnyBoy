from django.contrib import admin
from django.urls import path
from asistencia.views import (
    # Públicas
    registrar_chequeo,
    pantalla_principal,
    obtener_registros_hoy,
    # Patrón - Login
    patron_login,
    patron_logout,
    patron_dashboard,
    # Patrón - Barberos
    patron_agregar_barbero,
    patron_editar_barbero,
    patron_eliminar_barbero,
    # Patrón - Registros
    patron_editar_registro,
    patron_eliminar_registro,
    patron_crear_registro_manual,
    # Reportes
    pagina_reportes,
    reporte_excel,
    reporte_pdf,
)

urlpatterns = [
    # Admin original de Django
    path('admin/', admin.site.urls),

    # APIs del ESP32 y del checador
    path('api/registrar/', registrar_chequeo, name='registrar_chequeo'),
    path('api/registros-hoy/', obtener_registros_hoy, name='registros_hoy'),

    # Pantalla pública del checador
    path('', pantalla_principal, name='pantalla_principal'),

    # PÁGINA DEL PATRÓN
    path('patron/login/', patron_login, name='patron_login'),
    path('patron/logout/', patron_logout, name='patron_logout'),
    path('patron/', patron_dashboard, name='patron_dashboard'),

    # CRUD Barberos
    path('patron/barbero/agregar/', patron_agregar_barbero, name='patron_agregar_barbero'),
    path('patron/barbero/<int:barbero_id>/editar/', patron_editar_barbero, name='patron_editar_barbero'),
    path('patron/barbero/<int:barbero_id>/eliminar/', patron_eliminar_barbero, name='patron_eliminar_barbero'),

    # CRUD Registros
    path('patron/registro/crear/', patron_crear_registro_manual, name='patron_crear_registro'),
    path('patron/registro/<int:registro_id>/editar/', patron_editar_registro, name='patron_editar_registro'),
    path('patron/registro/<int:registro_id>/eliminar/', patron_eliminar_registro, name='patron_eliminar_registro'),

    # Reportes (ahora bajo /patron/)
    path('patron/reportes/', pagina_reportes, name='pagina_reportes'),
    path('patron/reportes/excel/', reporte_excel, name='reporte_excel'),
    path('patron/reportes/pdf/', reporte_pdf, name='reporte_pdf'),
]