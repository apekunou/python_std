l_numbers = [1, 26, 8, 32, 13, 39, 107]

for num in l_numbers:
    mod = num % 13
    if mod <> 0:
        continue
    print(num)