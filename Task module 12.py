money = float(input("Введите сумму вклада "))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
stavka=list(map(float, per_cent.values()))
deposite=[i * int(money) / 100 for i in stavka]
print("Депозит", deposite)
b=max(deposite, key=lambda i: int(i))
print("Максимальная сумма, которую вы можете заработать", b)