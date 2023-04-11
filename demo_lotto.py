import random

lotto = []

while len(lotto)<6:
    check = True
    num = random.randint(1,50)
    for i in lotto:
        if i == num:
            check = False
    if check:
        lotto.append(num)

print(lotto)