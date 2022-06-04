per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = input("Введите денежную сумму, которую Вы планируете положить под проценты: ")
money = float(money)
tkb = round(money*per_cent['ТКБ']/100,2)
skb = round(money*per_cent['СКБ']/100,2)
vtb = round(money*per_cent['ВТБ']/100,2)
sber = round(money*per_cent['СБЕР']/100,2)
deposit = [tkb,skb,vtb,sber]
print("За год в банке ТКБ вы можете накопить —","%.2f" % (tkb))
print("За год в банке СКБ вы можете накопить —","%.2f" % (skb))
print("За год в банке ВТБ вы можете накопить —","%.2f" % (vtb))
print("За год в банке СБЕР вы можете накопить —","%.2f" % (sber))
print("Максимальная сумма, которую вы можете заработать —","%.2f" % (max(deposit)))