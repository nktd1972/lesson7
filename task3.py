def make_operation(operator, *numbers):
    if operator == '*':
        result = 1
    else:
        result = 0
    for num in numbers:
        if operator == '+':
            result += num
        elif operator == '-':
            result -= num
        elif operator == '*':
            result *= int(num)
    return result


print(make_operation('+', 7, 7, 2))

