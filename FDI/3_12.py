# Leer tres números correspondientes al día, mes y año de una fecha e imprimir
# un mensaje indicando si la fecha es válida o no.

día = int(input("Ingrese día: "))
mes = int(input("Ingrese mes: "))
año = int(input("Ingrese año: "))

AÑO_ACTUAL = 2020
es_año_bisiesto = (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)
es_mes_de_30_días = mes in [4, 6, 9, 11]
es_mes_de_31_días = mes in [1, 3, 5, 7, 8, 10, 12]
es_fecha_válida = False

if mes <= 12 and año <= AÑO_ACTUAL:

    # meses con 30 días
    if es_mes_de_30_días and día <= 30:
        es_fecha_válida = True

    # meses con 31 días
    elif es_mes_de_31_días and día <= 31:
        es_fecha_válida = True

    # febrero en año bisiesto
    elif (es_año_bisiesto) and día <= 28:
        es_fecha_válida = True

    # febrero en año no bisiesto
    elif mes == 2 and día <= 29:
        es_fecha_válida = True


if (es_fecha_válida):
    print("La fecha ingresada es válida")
else:
    print("La fecha ingresada no es válida")
