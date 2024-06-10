import datetime
import time

def obtener_fecha_hora_actual():
        ahora = datetime.datetime.now()
        fecha_formateada = ahora.strftime("%d/%m/%y %I:%M%p")
        print(fecha_formateada)
        # time.sleep(1)  # Espera 1 segundo antes de actualizar nuevamente

obtener_fecha_hora_actual()
