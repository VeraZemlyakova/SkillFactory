print("Заказ билетов для участия в онлайн-конференции.")
while True:
    try:
        n = int(input("Введите количество билетов, которые Вы хотите приобрести: \t"))
    except ValueError:
        print('Введите натуральное число, пожалуйста.')
        continue
    else:
        if n <= 0:
            print("В заказе должен быть хотя бы один билет.")
            continue
        break
sum = 0
for i in range(1,n+1):
    while True:
        age = input(f"Введите возраст {i}-го участника конференции: \t")
        try:
            age = int(age)
        except ValueError:
            print("Введите натуральное число, пожалуйста.")
            continue
        else:
            if 18 <= age < 25:
                sum += 990
            elif age >= 25:
                sum += 1390
                if age > 100:
                    print("Мы рады участию долгожителя в нашей конференции!")
            elif age < 0:
                print("Неверно указан возраст.")
                continue
            break
if sum == 0:
    print("Посетители до 18 лет, могут принять участие в конференции бесплатно.")
else:
    if n > 3:
        sum *= 0.9
    print("Cумма к оплате:\t","%.2f" % (round(sum,2)),"руб.")






