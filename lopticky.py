import random
vysledky=[0]+[0]*12
for i in range(1000000):
    vysledky[random.randint(1,6)+random.randint(1,6)]+=1
for i,j in enumerate(vysledky):
    print(i, 'fell', round(100/1000000*vysledky[i],2),'%')