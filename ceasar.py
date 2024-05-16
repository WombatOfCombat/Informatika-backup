end_state=''
word=input('word to encode:')
code_number=int(input('code number:'))
spaces_list=[]
for y,x in enumerate(word):
    if x==' ':
        spaces_list.append(y)
word.replace(' ','')
for i in enumerate(word):
    if i[1]==' ':
        end_state+=' '
    else:
        end_state+=(chr(((ord(i[1])+code_number-97)%25)+97))
print(end_state)        
