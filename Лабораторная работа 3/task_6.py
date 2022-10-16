list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

index_max = list_numbers.index(max(list_numbers)) # индекс максимального элемента
list_numbers[-1], list_numbers[index_max] = list_numbers[index_max], list_numbers[-1]

print(list_numbers)
