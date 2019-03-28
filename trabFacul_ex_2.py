print('Deixe seu curriculo no empregos.com')
pro = str(input('Digite a profissão desejada: ')).upper()
gen = str(input('Digite seu gênero(M/F): ')).upper()
id = int(input('Digite sua idade: '))
grad = str(input('Qual é a sua Graduação: ')).upper()
s = gen[0]

if pro == 'ENFERMEIRA' and id >= 25 or id <= 35 and s == 'F' and grad == 'ENFERMAGEM':
    print(f'Temos uma de vaga {pro} relacionada ao seu perfil cadastrado')
elif pro == 'PROGRAMADOR' and id >= 20 or id <=30 and s == 'M' and grad == 'CIÊNCIA DA COMPUTAÇÃO' or grad == 'TADS':
    print(f'Temos uma de vaga {pro} relacionada ao seu perfil cadastrado')
elif pro == 'ANALISTA DE SEGURANÇA' and s == 'M' and grad == 'TSEG':
    print(f'Temos uma de vaga {pro} relacionada ao seu perfil cadastrado')
else:
    print('É só aguardar. Obrigado e tenha um bom dia!')
    #print('Nenhuma vaga foi encontrada para o perfil informado!')