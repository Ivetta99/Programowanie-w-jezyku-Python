def multiply_list_for(numbers):
    result = []
    for number in numbers:
        result.append(number * 2)
    return result


print(multiply_list_for([2, 3, 4, 2, 1]))


def multiply_list(numbers):
    return [number * 2 for number in numbers]


print(multiply_list([2, 3, 4, 2, 1]))
