from django.contrib import admin
from django.urls import path
from asistencia.views import registrar_chequeo, pantalla_principal, obtener_registros_hoy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/registrar/', registrar_chequeo, name='registrar_chequeo'),
    path('api/registros-hoy/', obtener_registros_hoy, name='registros_hoy'),
    path('', pantalla_principal, name='pantalla_principal'),
]