Prime_number = [2]
current = 3
while True:
    for num in Prime_number:
        if current%num == 0:
            Prime_number.append(current)
            if current > 10000:
                print(current + '\n')
            break
    current+=1