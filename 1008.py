numero = int(input("Digite seu número:"))
horas_trabalhadas = int(input("Quantas horas voce trabalha por dia?"))
valor_hora = float(input("Qual o valor voce recebe por hora?"))

salario = valor_hora * horas_trabalhadas

print(f'NUMBER = {numero}')
print(f'SALARY = U$ {salario:.2f}')