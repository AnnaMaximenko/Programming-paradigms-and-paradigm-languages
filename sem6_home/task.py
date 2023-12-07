def binary_search(array, start_element, key):
    end_element = len(array) - 1
    while start_element <= end_element:
        middle_element = start_element + (end_element - start_element) // 2
        if array[middle_element] == key:
            return middle_element
        elif array[middle_element] < key:
            start_element = middle_element + 1
        else:
            end_element = middle_element - 1
    return -1



array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
find_element = 3

result = binary_search(array, 0, find_element)
print(result)


# В данном примере выбраны:
# 1) Структурная парадигма
# Так как, для решения, нам необходима быстрая разработка небольшой программы, которую не
# планируется расширять в ближайшее время
# 2) Процедурное программирование, так как части кода можно использовать несколько раз
