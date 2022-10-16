salary = 5000
spend = 6000
months = 10
increase = 0.03
grow_price = increase + 1

# задаём изначальное условие
# 0 говорит о том, что один день мы можем себе позволить прожить бесплатно
need_money = 0

for money in range(1, months + 1):
    money = spend - salary
    spend = spend * grow_price
    need_money += money #количество денег, необходимую для того, чтобы прожить 10 мес.

print(round(need_money))
