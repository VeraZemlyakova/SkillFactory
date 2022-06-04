per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input("Введите денежную сумму, которую Вы планируете положить под проценты: "))
deposit = list()
for key, val in per_cent.items():
    deposit.append(round(money*val/100,2))
    print("За год в банке",key,"вы можете накопить —","%.2f" % (deposit[-1]))
print("Максимальная сумма, которую вы можете заработать —","%.2f" % (max(deposit)))