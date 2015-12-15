a = 6
b = 8
c = 3
sum = 0

if a > b:
    sum = sum + a
    if c > b:
        sum = sum + c
    else:
        sum = sum + b
else:
    sum = sum + b
    if c > a:
        sum = sum + c
    else:
        sum = sum + a

print(sum)