def personal_sum(numbers):
    incorrect_data = 0
    result = 0
    for i in numbers:
        try:
            result += i
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчета суммы - {i}')
    return result, incorrect_data


def  calculate_average(numbers):
        try:
            a = personal_sum(numbers)
            b = []
            for j in numbers:
                if type(j) == int:
                    b.append(j)
            return a[0] / len(b)
        except ZeroDivisionError:
            return 0
        except TypeError:
            print('В numbers записан некорреткный тип данных')



print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать