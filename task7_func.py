def price_calculate(kg, price):
    sum = kg * price
    sum_r = round(sum)
    return sum_r

kg = 1.34
price = 10
sum_res = price_calculate(kg, price)
print(sum_res)
