print(list(filter(None,list(map(lambda x: x if (x % 4 or x % 400 and x % 100 < 1) < 1 else '',range(2021, 2040))))))