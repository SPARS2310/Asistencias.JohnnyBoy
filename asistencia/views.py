import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Empleado, Registro

# Usamos csrf_exempt para que tu placa electrónica pueda enviar datos
# sin ser bloqueada por los sistemas de seguridad web de Django.
@csrf_exempt
def registrar_chequeo(request):
    if request.method == 'POST':
        try:
            # Leemos el dato enviado por el lector RFID
            data = json.loads(request.body)
            uid_recibido = data.get('uid')

            # Buscamos si el UID existe en la base de datos
            empleado = Empleado.objects.filter(uid_rfid=uid_recibido).first()
            
            if not empleado:
                return JsonResponse({'status': 'error', 'mensaje': 'Tarjeta no registrada'}, status=404)

            # Buscamos el último registro de ese empleado
            ultimo_registro = Registro.objects.filter(empleado=empleado).order_by('-fecha_hora').first()

            # Determinamos si es Entrada o Salida
            if ultimo_registro and ultimo_registro.tipo == 'ENTRADA':
                nuevo_tipo = 'SALIDA'
            else:
                nuevo_tipo = 'ENTRADA'

            # Guardamos el nuevo registro
            Registro.objects.create(empleado=empleado, tipo=nuevo_tipo)

            return JsonResponse({
                'status': 'success', 
                'empleado': empleado.nombre, 
                'accion': nuevo_tipo
            })

        except Exception as e:
            return JsonResponse({'status': 'error', 'mensaje': str(e)}, status=400)

    return JsonResponse({'status': 'error', 'mensaje': 'Metodo no permitido. Usa POST.'}, status=405)