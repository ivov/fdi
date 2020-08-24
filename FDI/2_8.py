# Una inmobiliaria paga a sus vendedores un salario de $800, más una comisión de
# $50 por cada venta realizada, más el 5% del valor de esas ventas. Realizar un
# programa que imprima el número del vendedor y el # salario que le corresponde
# en un determinado mes. Se leen el número del vendedor, la cantidad de ventas
# que realizó y el valor total de las mismas.

BASE_SALARIAL = 800
COMISION_POR_VENTA = 50
PORCENTAJE_POR_TOTAL_DE_VENTAS = 0.05

numero_vendedor = input("Ingrese el número del vendedor: ")
cantidad_de_ventas = int(input("Ingrese la cantidad de ventas: "))
valor_total_de_ventas = int(input("Ingrese el valor total de las ventas: "))

haberes = (
    BASE_SALARIAL + cantidad_de_ventas * COMISION_POR_VENTA +
    valor_total_de_ventas * PORCENTAJE_POR_TOTAL_DE_VENTAS
)

print("Los haberes del vendedor n.° %s son $%d" % (numero_vendedor, haberes))
