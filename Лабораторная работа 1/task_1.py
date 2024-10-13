numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
sum_n = sum(numbers[0:4:]) + sum(numbers[5::])
len_n = len(numbers)
r = sum_n/len_n
numbers[4] = r
print("Измененный список:", numbers)
