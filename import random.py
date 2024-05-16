import random,tkinter,time
while True:
    text=''
    time.sleep(0.1)
    for _ in range(255):
        text+=random.choice(['(',']','-','_','"','=','+','-','0','1','*','\\','/'])
    print(text[:255])