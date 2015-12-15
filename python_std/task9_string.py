def print_odd(*args):
    for num in args:
        even = num % 2
        if even == 0:
            print("An even number {}". format(num))
        else:
             print("An odd number {}". format(num))

print_odd(2, 5, 7, 8, 321)
