# Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:

# — символ «?» означает ровно одну произвольную цифру;

# — символ «*» означает любую последовательность цифр произвольной длины; в том числе «*» может задавать и пустую последовательность.

# Например, маске 123*4?5 соответствуют числа 123405 и 12300405.

# Среди натуральных чисел, не превышающих 1010, найдите все числа, соответствующие маске 1?2157*4, делящиеся на 2024 без остатка. В ответе запишите в первом столбце таблицы все найденные числа в порядке возрастания, а во втором столбце  — соответствующие им результаты деления этих чисел на 2024.

def matches_mask(number):
    mask ="1?2157*4"
    number_str=str(number)
    if len(mask) != len(number_str):
        return False
    
    for i in range(len(mask)):
        if mask[i]=="?":
            if not number_str[i].isdigit():
                return False
            
    for i in range(len(mask)):
        if mask[i] == "?":
            if not number_str[i].isdigit():
                return False
        elif mask[i] == "*":
            if not number_str[i:].isdigit():
                return False
        elif mask[i] != number_str[i]:
            return False
    return True

results = []
for number in  range(1, 10100000000):
    if matches_mask(number) and number%2024==0:
        results.append((number, number//2024))

for result in results:
    print(results[0], results[1])