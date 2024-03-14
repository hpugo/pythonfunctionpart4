def max_num(num1, num2, num3):
    return max(num1, num2, num3)
result_max = max(1, 10, 100)
print(result_max)

def mult_list(num_list):
    result = 1
    for num in num_list:
        result *= num
    return result
result_multi = mult_list([5, 10, 2])
print(result_multi)

def rev_string(initial_string):
    return initial_string[::-1]
reversed_string = rev_string('Apples')
print(reversed_string)

def num_within(number, start, end):
    return start <= number <= end
false_result = num_within(10, 11, 200)
true_result = num_within(10, 2, 100)
print(false_result)
print(true_result)

def pascal(n):
    for i in range(n):
        row = [1]
        if i > 0:
            for j in range(1, i):
                val = row[j - 1] * (i - j + 1) // j
                row.append(val)
            row.append(1)
        print(" ".join(map(str, row)))

# Example usage:
pascal(5)
