nota = float(input('Insira a nota do aluno:  '))

if nota >= 9:
    print('Aprovado com honras')
elif nota >= 7:
    print('Aprovado')
elif nota >= 5:
    print('Recuperação')
else:
    print('Reprovado')
