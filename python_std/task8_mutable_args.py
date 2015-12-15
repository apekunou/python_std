def calc_numbers(*args):
    sum = 0
    for num in args:
        str_num = str(num)
        n = len(str_num)
        for i in range(0,n):
            sum = sum + int(str_num[i])
    return sum


sum = calc_numbers(111, 2, 33)
print(sum)