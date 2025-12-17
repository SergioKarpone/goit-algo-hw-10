import pulp

# Ініціалізація моделі для максимізації (LpMaximize) кількості продуктів
model = pulp.LpProblem("Maximize_Drink_Production", pulp.LpMaximize)

# Параметри: lowBound=0 (кількість напоїв >0), cat='Integer' (кількість пляшок)
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')

# Цільова функція - максимізація кількості (лимонад + фруктовий сік)
model += lemonade + fruit_juice, "Total_Number_of_Products"

# Обмеження ресурсів на воду (2 од. на лимонад + 1 од. на сік <= 100)
model += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Constraint"

# Обмеження на цукор (1 од. на Лимонад <= 50)
model += 1 * lemonade <= 50, "Sugar_Constraint"

# Обмеження на лимонний сік (1 од. на Лимонад <= 30)
model += 1 * lemonade <= 30, "Lemon_Juice_Constraint"

# Обмеження на фруктове пюре (2 од. на Сік <= 40)
model += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"

# Запуск моделі
model.solve()

# Результати
print(f"Статус розв'язку: {pulp.LpStatus[model.status]}\n")
print(f"Кількість 'Лимонаду' для виробництва: {lemonade.varValue}")
print(f"Кількість 'Фруктового соку' для виробництва: {fruit_juice.varValue}")
print(f"\nМаксимальна загальна кількість продуктів: {pulp.value(model.objective)}")
