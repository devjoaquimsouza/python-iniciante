import math
co = float(input('Informe o valor do cateto oposto do triângulo retângulo: '))
ca = float(input('Informe o valor do cateto adjacente desse triângulo: '))
hip = math.hypot(co, ca)
print('A hipotenusa é igual a {}.'.format(hip))