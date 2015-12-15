
The_Answer = "The Answer to the Ultimate Question of Life, the Universe, and Everything"

l_numbers = [1, 128, 48, 51, 138, 42, 59]

for num in l_numbers:
    if num == 42:
        print(The_Answer)
        break
    res = num / 100
    if res < 1.0:
        print(num)



