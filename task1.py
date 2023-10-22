money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
i = 0
while True:
    x = spend - salary
    if x > money_capital:
        break

    i += 1
    money_capital -= x
    spend *= 1 + increase

print("Количество месяцев, которое можно протянуть без долгов:", i)
