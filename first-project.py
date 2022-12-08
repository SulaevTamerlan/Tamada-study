number_1 = int(input('Введите число до которого нужно сделать таблицу: '))
if number_1 <= 10:
    print('Считай сам!')
else:
    for table in range(1, number_1 + 1):
        for n in range(1, 11):
            answer = table * n
            print(answer, end='\t')

        print('\n')

    print('Две минуты. Готово!')

