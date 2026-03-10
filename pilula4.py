import statistics 

#leitura
lote1 = float(input('Produção lote 1: '))
lote2 = float(input('Produção lote 2: '))
lote3 = float(input('Produção lote 3: '))

#processamento
media = statistics.mean( (lote1, lote2, lote3) )
desvio = statistics.stdev ( (lote1, lote2, lote3) )

#saída
print (f'Média: {media:.2f} ')
print (f'Desvio padrão: {desvio:.2f}')
