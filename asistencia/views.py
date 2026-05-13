import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Empleado, Registro


def pantalla_principal(request):
    """Muestra la pantalla principal del checador con los registros del día actual."""
    hoy = timezone.localdate()
    registros_hoy = (
        Registro.objects
        .filter(fecha_hora__date=hoy)
        .select_related('empleado')
        .order_by('-fecha_hora')
    )
    contexto = {
        'registros_hoy': registros_hoy,
        'total_hoy': registros_hoy.count(),
        'fecha_hoy': hoy,
    }
    return render(request, 'index.html', contexto)


def obtener_registros_hoy(request):
    """Endpoint que devuelve los registros del día en formato JSON (para auto-actualizar)."""
    hoy = timezone.localdate()
    registros = (
        Registro.objects
        .filter(fecha_hora__date=hoy)
        .select_related('empleado')
        .order_by('-fecha_hora')
    )
    data = [
        {
            'empleado': r.empleado.nombre,
            'tipo': r.tipo,
            'hora': timezone.localtime(r.fecha_hora).strftime('%H:%M:%S'),
        }
        for r in registros
    ]
    return JsonResponse({'registros': data, 'total': len(data)})


@csrf_exempt
def registrar_chequeo(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            uid_recibido = data.get('uid')
            empleado = Empleado.objects.filter(uid_rfid=uid_recibido).first()

            if not empleado:
                return JsonResponse({'status': 'error', 'mensaje': 'No registrado'}, status=404)

            ultimo = Registro.objects.filter(empleado=empleado).order_by('-fecha_hora').first()
            nuevo_tipo = 'SALIDA' if ultimo and ultimo.tipo == 'ENTRADA' else 'ENTRADA'

            Registro.objects.create(empleado=empleado, tipo=nuevo_tipo)
            return JsonResponse({'status': 'success', 'empleado': empleado.nombre, 'accion': nuevo_tipo})
        except Exception as e:
            return JsonResponse({'status': 'error', 'mensaje': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'mensaje': 'POST requerido'}, status=405)