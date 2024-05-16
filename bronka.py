while True:
    x=list()
    while True:
        x.append(input("Enter number or 'x':"))
        if x[0]=="x":
            print("Empty sequence")
            break
        elif x[-1]=="x":
            print("All numbers had the same digit in the ones place")
            break
        elif len(x)!=1 and (int(x[-2])-int(x[-1]))%10!=0:
            print(f"{x[-2]} and {x[-1]} differ in the ones place")
            break
        if len(x)>2:
            x.pop(-3)
