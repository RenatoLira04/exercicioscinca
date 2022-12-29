salario1 = float(input('Qual o sálario do funcionário? R$'))
salario2 = salario1 + (salario1 * 15 / 100)
print('O salário do funcionário de R${:.2f} será de R${:.2f} com 15% de aumento.'.format(salario1, salario2))
