print('Vai até aonde?')
dis = int(input('Quantos metros você irá percorrer? '))
if dis < 100:
    print('Vai andando')
elif dis >= 100 and dis < 500:
    print('vai de Bike')
elif dis >= 500 and dis < 1000000:
    print('Vai de carro')
elif dis >= 1000000:
    print('Vai de avião')