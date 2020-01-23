Prime_number = [2]
current = 3
judge = True
while True:
    for num in Prime_number:
        if current%num == 0:
            judge = False
    if judge == True:
        Prime_number.append(current)
        if current > 10000:
            print(current)
    judge = True
    current+=1