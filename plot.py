# пишем в консоль pip install matplotlib
import matplotlib.pyplot as plt
# y = 3x**3 + 5x**2 + 2x + 15
x = []
y = []
# все иксы
for i in range(21):
    x.append(i)
# найдем к ним игрики
for i in range(len(x)):
    y.append(3 * (x[i] ** 3) + 5 * (x[i] ** 2) + 2 * x[i] + 15)

plt.plot(x, y) #построим график
plt.xlabel('Ось х') #Подпись для оси х
plt.ylabel('Ось y') #Подпись для оси y
plt.title('График') #Название
plt.show() #вывод графика на экран