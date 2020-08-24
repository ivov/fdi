# Leer un período en segundos e imprimirlo expresado en días, horas, minutos
# y segundos. Por ejemplo, 200_000 segundos equivalen a 2 días, 7
# horas, 33 minutos y 20 segundos.

SEGUNDOS_POR_MINUTO = 60
SEGUNDOS_POR_HORA = 60 * SEGUNDOS_POR_MINUTO
SEGUNDOS_POR_DÍA = 24 * SEGUNDOS_POR_HORA

tiempo_en_segundos = int(input("Ingrese segundos: "))

# dividir por d/h/m para número entero, extraer restos y operar sobre restos

días = tiempo_en_segundos // SEGUNDOS_POR_DÍA
tiempo_en_segundos = tiempo_en_segundos % SEGUNDOS_POR_DÍA

horas = tiempo_en_segundos // SEGUNDOS_POR_HORA
tiempo_en_segundos = tiempo_en_segundos % SEGUNDOS_POR_HORA

minutos = tiempo_en_segundos // SEGUNDOS_POR_MINUTO
tiempo_en_segundos = tiempo_en_segundos % SEGUNDOS_POR_MINUTO

print("%d días, %d horas, %d minutos, %d segundos" %
      (días, horas, minutos, tiempo_en_segundos))
