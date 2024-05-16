import random
y=0
ite=1000000
for _ in range(ite):
    if random.randint(1,6)+random.randint(1,6)<3:
        y+=1
print(y/ite*100)
