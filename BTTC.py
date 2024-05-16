import math
x=0
y=0
txt=''
while True:
    user_input='e'
    while not user_input.isnumeric():
        user_input=input('input binary string 8 digits at a time\n write end when all code is written:')
        if user_input=='end':
            print(txt)
            txt=''
    txt+=chr(int(user_input,2))
print(txt)
