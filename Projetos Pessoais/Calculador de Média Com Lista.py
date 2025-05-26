lista=[]
while True:
    n=float(input('Digite a nota do aluno: '))
    if n==-1:
        break
    lista.append(n)
print(f'A média das notas dos alunos é {sum(lista)/len(lista)}')