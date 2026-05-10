from django.contrib import admin
from django.urls import path
from asistencia.views import registrar_chequeo

urlpatterns = [
    path('admin/', admin.site.urls),
    # Esta es la URL a la que tu hardware enviará los datos:
    path('api/registrar/', registrar_chequeo, name='registrar_chequeo'),
]