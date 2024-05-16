import random
import colorama
from colorama import Fore, Style
temperature_list=[]
maximum_temperature_list=[]
minimum_temperature_list=[]
for _ in range(10*24):
    temperature_list.append(random.randint(10,30))
maximum_temperature=temperature_list[0]
for temperature in temperature_list:
    if temperature>maximum_temperature:
        maximum_temperature=temperature
for i in range(len(temperature_list)):
    if temperature_list[i]==maximum_temperature:
        maximum_temperature_list.append([(i//24)+1,(i+1)%24,i])
minimum_temperature=temperature_list[0]
for temperature in temperature_list:
    if temperature<minimum_temperature:
        minimum_temperature=temperature
for i in range(len(temperature_list)):
    if temperature_list[i]==minimum_temperature:
        minimum_temperature_list.append([(i//24)+1,(i+1)%24,i])
print('the maximum of {}°C temperature was recorded in the following times:'.format(maximum_temperature))
for time in maximum_temperature_list:
    print('{}. day, {}. hour (list index {})'.format(time[0],time[1],time[2]))
print('the minimum temperature of {} was recorded in the following times:'.format(minimum_temperature))
for time in minimum_temperature_list:
    print('{}. day, {}. hour (list index {})'.format(time[0],time[1],time[2]))
day_list=[temperature_list[i:i + 24] for i in range(0, len(temperature_list), 24)]
for i in range(len(day_list)):
    print('day {}:{}'.format(i+1,day_list[i]))

price_list=[]
full_price=0
for i in range(20):
    price_list.append(random.randint(150,2500))
for price in price_list:
    full_price+=price
print('The full price is {}€.'.format(full_price/100))
most_expensive=price_list[0]
for price in price_list:
    if most_expensive<price:
        most_expensive=price
print('The most expensive item costs {}€.'.format(most_expensive/100))
least_expensive=price_list[0]
for price in price_list:
    if least_expensive>price:
        least_expensive=price
print('The least expensive item costs {}€.'.format(least_expensive/100))
print('The average price of an item is {}€.'.format(full_price/len(price_list)/100))
for i in range(len(price_list)):
    print('The {}. item costs {}€.'.format(i+1,price_list[i]/100))
