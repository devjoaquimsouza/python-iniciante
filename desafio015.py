km = float(input('Km percorridos: '))
dias = float(input('Dias alugados: '))
precofinal = (km * 0.15) + (dias * 60)
print('O preço a pagar será de R${:.2f}'.format(precofinal))