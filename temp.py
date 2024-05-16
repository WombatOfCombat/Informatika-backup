import random

temp_list=[21]

for i in range(29):
    new_temp=temp_list[i]+random.randint(-5,5)
    if new_temp>=38 or new_temp<=15:
        new_temp=21
    temp_list.append(new_temp)

print(temp_list)

average_sum=0

for temp in temp_list:
    average_sum+=temp
print(average_sum//len(temp_list))

