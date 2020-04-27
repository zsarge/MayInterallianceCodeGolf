for x in range(2021, 2040):
    if x % 4 == 0 and x % 100 != 0 or x % 400 == 1:
        print(x)

# Should output: 2024 2028 2032 2036 