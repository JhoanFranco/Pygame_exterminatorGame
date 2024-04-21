import time

class Cronometro:
    def __init__(self):
        self.inicio = None
        self.fin = None

    def iniciar(self):
        self.inicio = time.time()

    def detener(self):
        self.fin = time.time()

    def reiniciar(self):
        self.inicio = None
        self.fin = None

    def obtener_tiempo_transcurrido(self):
        if self.inicio is None:
            return 0
        elif self.fin is None:
            return time.time() - self.inicio
        else:
            return self.fin - self.inicio

    def obtener_tiempo_formateado(self):
        tiempo_transcurrido = self.obtener_tiempo_transcurrido()

        minutos, segundos = divmod(tiempo_transcurrido, 60)
        segundos_enteros, milisegundos = divmod(segundos, 1)

        return int(minutos), int(segundos_enteros), int(milisegundos * 1000)

# # Ejemplo de uso
# cronometro = Cronometro()

# input("Presiona Enter para iniciar el cronómetro...")
# cronometro.iniciar()

# input("Presiona Enter para detener el cronómetro...")
# cronometro.detener()

# minutos, segundos, milisegundos = cronometro.obtener_tiempo_formateado()
# print("Tiempo transcurrido:", minutos, "minutos", segundos, "segundos", milisegundos, "milisegundos")
