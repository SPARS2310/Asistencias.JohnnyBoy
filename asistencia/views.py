import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Empleado, Registro

def pantalla_principal(request):
    return render(request, 'index.html')

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