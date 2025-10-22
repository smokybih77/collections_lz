print('Введите до какого числа (порядкового) будет ряд Фибоначчи:')
N = int(input())
if N < 2 :
    print('Ряда Фибоначчи не будет') #По определению он начинается с 0 и 1
else:
    fib = list()
    fib.append(0)
    fib.append(1)
    for i in range(N-2):
        i = 0
        f = fib[i-1]+fib[i-2]
        i += 1
        fib.append(f) #складываем предыдущие 2 элемента для получения следующего
    print('Ряд Фибоначчи:', fib)
    for i in range(len(fib)):
        if i % 2 == 1:
            fib[i] = fib[i] * 2
        else:
            fib[i] = fib[i] ** 2
    print('Преобразованный ряд Фибоначчи:') # меняем ряд в связи с условием
    print(fib)
    min = 0 #очевидно
    max = 0
    for i in range(len(fib)):
        if fib[i] > max:
            max = fib[i]
    print('Минимальный элемент:', min)
    print('Максимальный элемент:', max)
    print('Длина списка:', N) #дано в условии
    summ = 0
    for i in range(len(fib)): # пройдем по списку и сложим все значения
        summ += fib[i]
    kk = summ / len(fib) # найдем среднее среди них
    mdzn = 0
    for i in range(len(fib)): # сравним все элементы со средним и найдем то, что нужно
        if fib[i] > kk: 
            mdzn += 1
    print('Количество элементов, больших медианного значения:', mdzn)