numbers=[4,1,2,7,6,9]

def sort_list_imperative(numbers):
    for i in range(1, len(numbers)):
        number = numbers[i]
        pos = i
        while pos > 0 and numbers[pos - 1] < number:
            numbers[pos] = numbers[pos - 1]
            pos -= 1
        numbers[pos] = number
    pass
    return numbers

def sort_list_declarative(numbers):
    numbers.sort(reverse=True)
    pass
    return numbers


print(sort_list_imperative(numbers))

print(sort_list_declarative(numbers))