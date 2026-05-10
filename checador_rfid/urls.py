from django.contrib import admin
from django.urls import path
from asistencia.views import registrar_chequeo, pantalla_principal

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/registrar/', registrar_chequeo, name='registrar_chequeo'),
    path('', pantalla_principal, name='pantalla_principal'),
]