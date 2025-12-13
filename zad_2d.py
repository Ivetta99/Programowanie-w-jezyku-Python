def print_odd_numbers(numbers):
    for i in range(0, len(numbers), 2):
        print(numbers[i])


number_list = list(range(1, 11))
print_odd_numbers(number_list)
