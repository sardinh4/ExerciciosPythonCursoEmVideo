from ex109 import moeda

p = float(input('Digite um preço: R$'))

print(f'A metade de {moeda.moeda(p)} é igual a {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é igual a {moeda.dobro(p, True)}')
print(f'Aumentando em 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo o valor em 13%, temos {moeda.diminuir(p, 13, True)}')
