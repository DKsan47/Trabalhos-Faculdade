print('Voto Facultativo x Voto Obrigatório')
id = int(input('Digite sua idade: '))

if id >= 16 and id < 18 or id > 70:
    print(f'Sua idade é de {id} anos, portanto seu voto é facultativo')
else:
    print(f'Sua idade é de {id} anos, portanto o seu voto é obrigatório')