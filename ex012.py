valor1 = float(input('Qual o preço do produto:R$'))
valor2 = valor1 - (valor1 * 5 / 100)
print('O produto que custa R${:.2f}, custará R${:.2f} com 5% de desconto.'.format(valor1, valor2))
