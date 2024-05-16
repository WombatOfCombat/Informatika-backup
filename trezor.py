import random
c=0
a=0
grade_list=[85,70,50,20,0]
streak=[]
while True:  # Set a limit to the number of questions
    if random.choice([True,False]):
        sign='/'
        number2=random.randint(1,10)
        number1=random.randint(1,10)*number2
        result=number1/number2
    else:
        sign='x'
        number2=random.randint(1,10)
        number1=random.randint(0,10)
        result=number1*number2
    user_input=int(input('{}{}{}='.format(number1,sign,number2)))
    if user_input==result:
        print('Correct!')
        c+=1
        streak.append(True)
    else:
        print('Incorrect, the answer was',result)
        streak.append(False)
    a+=1
    if len(streak)>=3 and all(streak[-3:]):
        print('COMBO','!'*len(streak[max((i for i,value in enumerate(streak) if not value),default=None):]))
    percentage=round(100 / a * c, 2)
    print('Your success rate is',percentage,'%')
    for grade,percentage_required in enumerate(grade_list):
        if percentage>=percentage_required:
            print('Your grade is:',grade+1)
            break


