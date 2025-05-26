n1=int(input('Digite o número inicial da sequência: '))
n2=int(input('Digite o número final da sequência: '))
print('Fahrenheit / Celsius')
if n2>=n1:
    for f in range(n1, n2+1):
      print(f'{f:>10} / {5/9*(f-32):.2f}')
else:
    for f in range(n1, n2+1, -1):
      print(f'{f:>10} / {5/9*(f-32):.2f}')
