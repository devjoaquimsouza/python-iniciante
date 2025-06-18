nome = str(input('Digite seu nome completo: '))
nomeE = nome.replace(' ', '' )
nomeD = nome.split()

print('Este é seu nome em maiúsculas >> {}'.format(nome.upper()))
print('Este é seu nome em minúsculas >> {}'.format(nome.lower()))
print('{} letras compõem o seu nome completo'.format(len(nomeE)))
print('{} letras compõem o seu primeiro nome'.format(len(nomeD[0])))
