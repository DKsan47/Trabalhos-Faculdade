ra = int(input('Digite seu RA: '))
n = str(ra)
if ra >= 510 and ra <= 519:
    print(f'{n[0]} - Campus Memorial')
    print(f'{n[1]} - Curso Segurança da Informação')
    print(f'{n[2]} - ID Aluno')
elif ra >= 520 and ra <= 529:
    print(f'{n[0]} - Campus Memorial')
    print(f'{n[1]} - Curso Ciência da Computção')
    print(f'{n[2]} - ID Aluno')
elif ra>= 610 and ra <=619:
    print(f'{n[0]} - Campus Vergueiro')
    print(f'{n[1]} - Curso Segurança da Informação')
    print(f'{n[2]} - ID Aluno')
elif ra>= 620 and ra <= 629:
    print(f'{n[0]} - Campus Vergueiro')
    print(f'{n[1]} - Curso Ciência da Computação')
    print(f'{n[2]} - ID Aluno')
else:
    print('Aluno não matriculado!')