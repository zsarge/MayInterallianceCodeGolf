print(list(filter(None,map(lambda x:x if(x%400 and x%100<1or x%4)<1else'',range(2021, 2040)))))