numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
i = 4
sum_n = sum(numbers[:i:]) + sum(numbers[i+1::])
len_n = len(numbers)
numbers[4] = sum_n/len_n
print("Измененный список:", numbers)
