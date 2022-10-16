money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

# изначальное условие
month = 0
grow_spends = increase + 1 # рост расходов
ostatok = salary - spend
while money_capital + ostatok >= spend:
    money_capital += ostatok
    spend = spend * grow_spends
    month += 1 # количество месяцев, которое можно прожить

print(month)
