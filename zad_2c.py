def print_even_number(numbers):
    for number in numbers:
        if number % 2 == 0:
            print(number)

number_list = list(range(1, 11))
print_even_number(number_list)