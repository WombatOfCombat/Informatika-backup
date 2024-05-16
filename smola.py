import os,random
os.chdir(os.path.dirname(os.path.abspath(__file__))) #toto pridavam lebo moj pocitac ma divne nastavene directory (premeni to directory programu na lokaciu programu)
raw_read=[]
with open('meno.txt','r') as file:
    new_line=file.readline().replace('\n','')
    while new_line!='':
        raw_read.append(new_line if not new_line.isnumeric() else int(new_line))
        new_line=file.readline().replace('\n','')
segmented_read=[[raw_read[i],raw_read[i+1],raw_read[i+2]] for i in range(0,len(raw_read),3)]
print(segmented_read)
attendance=[0]*2
completed_exercises=[]
for student in segmented_read:
    for i in range(1,3):
        attendance[i-1]+=student[i]
    completed_exercises.append([student[0]]+[random.randint(0,5) if student[i] else 0 for i in range(1,3)])
    completed_exercises[-1].append(completed_exercises[-1][1]+completed_exercises[-1][2])
for i,value in enumerate(attendance):
    print(f'{i+1}. školenia sa zúčastnili/o {value} študenti/ov.')
best_student_indexes=[0]*3
for i,student in enumerate(completed_exercises):
    print(f'{student[0]} dostal {student[1]} bodov v prvom skoleni a {student[2]} bodov v druhom skoleni')
    for j,leading in enumerate(best_student_indexes):
        if student[j+1]>completed_exercises[leading][j+1]:
            best_student_indexes[j]=i
print(best_student_indexes)
best_students=[[] for _ in range(3)]
for i,student in enumerate(completed_exercises):
    for j,leading in enumerate(best_student_indexes):
        if student[j+1]==completed_exercises[leading][j+1]:
            best_students[j].append(i)
print(best_students)
for s,indexes in enumerate(best_students):
    if s==0:
        print('v prvom skoleni boli najlepsi ',end='')
    if s==1:
        print('v druhom skoleni boli najlepsi ',end='')
    if s==2:
        print('celkovo mali najviac bodov ',end='')
    for i in indexes:
        print(completed_exercises[i][0],end=' ')
    print('\n')