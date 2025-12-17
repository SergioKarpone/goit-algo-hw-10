import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi
import random

# Функція
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Кількість випадкових точок (більше - вища точність)
N = 100000 

# Генерація випадкових точок X в межах [a, b]
x_rand = np.random.uniform(a, b, N)

# Для Y шукаємо max функції на [a,b] - Y від 0 до 4
y_max = f(b) 
y_rand = np.random.uniform(0, y_max, N)

# Точка є під кривою, якщо її координата y_rand < f(x_rand)
under_curve = y_rand < f(x_rand)
count_under = np.sum(under_curve)

# Площа прямокутника з точками (ширина * висота)
rect_area = (b - a) * y_max

# Площа під кривою = (кількість під кривою / всього точок) * площа прямокутника
mc_result = (count_under / N) * rect_area

print(f"Кількість точок: {N}")
print(f"Результат методом Монте-Карло: {mc_result}")

# Перевірка за допомогою quad (аналітично)
quad_result, error = spi.quad(f, a, b)
print(f"Результат за допомогою quad: {quad_result}")

# Абсолютна похибка
abs_error = abs(mc_result - quad_result)
print(f"Абсолютна похибка: {abs_error}")

# Візуалізація
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots(figsize=(8, 6))

# Малювання функції
ax.plot(x, y, 'r', linewidth=2, label='f(x)=x^2')

# Заповнення області інтеграла (під кривою)
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3, label='Площа (Integal)')

# Візуалізація методу Монте-Карло (перші 200 точок)
ax.scatter(x_rand[:200], y_rand[:200], color='blue', s=10, alpha=0.5, label='Випадкові точки')

# Межі
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title(f'Метод Монте-Карло: f(x)=x^2, N={N}')
ax.legend()
plt.grid()
plt.show()
