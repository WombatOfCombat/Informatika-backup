x=0
for i in range(0,1000,7):
    x+=i
print(x)
#====================================================================================#
listcisiel=list()
for i in range(100,1000):
    sucetcifier=0
    s=str(i)
    for j in range(3):
        sucetcifier+=int(s[j])
    if sucetcifier%7==0:
        listcisiel.append(i)
print('cisla su:',listcisiel)
print('cisiel je',len(listcisiel))
