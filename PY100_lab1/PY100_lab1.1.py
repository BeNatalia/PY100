numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
# TODO заменить значение пропущенного элемента средним арифметическим
#len_numb = int(len(numbers))
#sum_numb = sum(numbers[:4] + numbers[5:])
#numbers[4] = sum_numb / len_numb
numbers[4] = sum(numbers[:4] + numbers[5:]) / len(numbers)
print("Измененный список:", numbers)
