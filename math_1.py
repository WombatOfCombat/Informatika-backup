from itertools import permutations
digits = [1,2,3,4,5,6,7,8,9]
permuted_digits = permutations(digits,9)
combinations=[''.join(map(str, p)) for p in permuted_digits]
all_sums=[]
sum_to_combinations={}
for combination in combinations:
    sums=[]
    for i in range(len(combination)-2):
        three_digits = combination[i:i+3]
        total = sum(int(digit) for digit in three_digits)
        sums.append(total)
    sums.append(int(combination))
    sums.sort()
    print(sums)
    all_sums.append(sums)
    sum_tuple = tuple(sums[:-1])
    if sum_tuple in sum_to_combinations:
        sum_to_combinations[sum_tuple].append(combination)
    else:
        sum_to_combinations[sum_tuple]=[combination]
all_sums.sort(key=lambda x:x[0])
def find_combinations_from_sums(sums_to_find):
    return sum_to_combinations.get(tuple(sums_to_find),[])
input_sums = [11,15,16,18,19,21,22]
output_combinations=find_combinations_from_sums(input_sums)
print("Input sums:",input_sums)
if output_combinations:
    print("Output combinations:")
    for combination in output_combinations:
        print(combination)
else:
    print("No combinations found for the input sums.")
