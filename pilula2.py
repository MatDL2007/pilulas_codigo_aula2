import random

#leitura
cotacao = float (input('Digite a cotacao atual do dolar: '))

#processamento
variacao = random.uniform(-0.015, 0.015)
nova_cotacao = cotacao * (1 + variacao)

#saída
print (f'Variação simulada: {variacao:.3%} ')
print (f'Nova cotação: {nova_cotacao:.2} ' )

