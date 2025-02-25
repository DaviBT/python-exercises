import math 

altura = float(input("altura: "))
raio = float(input("raio: "))

PI =  3.1415
circunferencia = 2 * PI * raio
areaTopo = PI * (raio * raio)
area = (circunferencia * altura) + areaTopo
area = round(area, 2)
print(f"área a ser pintada: {area}")

eficienciaLitro = 3
litrosNecessarios = area / eficienciaLitro
litrosNecessarios = round(litrosNecessarios, 2)
print(f"qtde. de litros necessários: {litrosNecessarios}")

lataTintaLitro = 5
latasNecessarias = math.ceil(litrosNecessarios/lataTintaLitro)
print(f"qtde. de latas necessárias: {latasNecessarias}")

precoUnit = float
if latasNecessarias == 1:
    precoUnit = 50.00
    print(f"Preco unitario: R$ {precoUnit}")
elif latasNecessarias == 2:
    precoUnit = 48.00
    print(f"Preco unitario: R$ {precoUnit}")
elif latasNecessarias == 3:
    precoUnit = 46.00
    print(f"Preco unitario: R$ {precoUnit}")
else:
    precoUnit = 45.00
    print(f"Preco unitario: R$ {precoUnit}")

precoTot = latasNecessarias * precoUnit
print(f"custo total: {precoTot}")