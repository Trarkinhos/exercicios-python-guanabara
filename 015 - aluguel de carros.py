# Code:
dias = int(input('Quantos dias esteve com o carro? '))
km = int(input('Quantos KM foram percorridos? '))
print(' Você utilizou o carro por {} dias e rodou {}km, abaixo estão os valores:'
      .format(dias, km))
print(' Total dos dias: R${} | Valor da diária: R$60.00 \n Total dos km: R${} | Valor por km: R$0.15 \n Valor total do aluguel: R${}'
      .format((dias * 60), (km * 0.15), ((dias * 60) + (km * 0.15))))
