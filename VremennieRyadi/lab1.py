import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('EuStockMarkets.csv')

# x_values = df['rownames']
DAX_values = df['DAX']
SMI_values = df['SMI']
CAC_values = df['CAC']
FTSE_values = df['FTSE']

plt.plot(DAX_values, color='blue', label='DAX')
plt.plot(SMI_values, color='red', label='SMI')
plt.plot(CAC_values, color='green', label='CAC')
plt.plot(FTSE_values, color='orange', label='FTSE')

plt.legend()

plt.title('График')
plt.xlabel('количество дней')
plt.ylabel('данные')
plt.grid(True)  # Добавление сетки

int_columns = ['CAC', 'DAX', 'FTSE', 'SMI']

correlation_matrix = df[int_columns].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Корреляционная матрица')

means = df[int_columns].mean()
variances = df[int_columns].var()

# # Построение гистограммы средних значений
plt.figure(figsize=(10, 5))
plt.bar(means.index, means.values, color='blue')
plt.xlabel('Столбцы')
plt.ylabel('Среднее значение')
plt.title('Средние значения столбцов')
plt.xticks(rotation=45)

# # Построение гистограммы дисперсий
plt.figure(figsize=(10, 5))
plt.bar(variances.index, variances.values, color='red')
plt.xlabel('Столбцы')
plt.ylabel('Дисперсия')
plt.title('Дисперсии столбцов')
plt.xticks(rotation=45)

# # столбцы однородны так как временной интервал одинаковый - 1 день

plt.show()

plt.figure(figsize=(10, 6))
plt.hist(DAX_values.abs(), bins=60, color='skyblue', edgecolor='black', alpha=0.7, label='DAX')
plt.hist(SMI_values.abs(), bins=60, color='salmon', edgecolor='black', alpha=0.7, label='SMI')
plt.hist(CAC_values.abs(), bins=60, color='green', edgecolor='black', alpha=0.7, label='CAC')
plt.hist(FTSE_values.abs(), bins=60, color='purple', edgecolor='black', alpha=0.7, label='FTSE')
plt.title('Гистограмма абсолютных значений')
plt.xlabel('Абсолютное значение')
plt.ylabel('Количество')
plt.legend()
plt.grid(True)

# # слева количество значений, снизу их диапазон

plt.figure(figsize=(10, 6))
plt.hist(DAX_values.diff().dropna(), bins=60, color='skyblue', edgecolor='black', alpha=0.7, label='DAX')
plt.hist(SMI_values.diff().dropna(), bins=60, color='salmon', edgecolor='black', alpha=0.7, label='SMI')
plt.hist(CAC_values.diff().dropna(), bins=60, color='green', edgecolor='black', alpha=0.7, label='CAC')
plt.hist(FTSE_values.diff().dropna(), bins=60, color='purple', edgecolor='black', alpha=0.7, label='FTSE')
plt.title('Гистограмма разностей')
plt.xlabel('Разница')
plt.ylabel('Количество')
plt.legend()
plt.grid(True)
plt.show()

# слева количество значений, снизу их диапазон
# -----------------------------------------------------------------------------------
# Диаграмма рассеяния без временного смещения

# plt.figure(figsize=(8, 6))
# plt.scatter(DAX_values, SMI_values, color='skyblue', alpha=0.7)
# plt.title('Диаграмма рассеяния двух временных рядов DAX и SMI')
# plt.xlabel('DAX')
# plt.ylabel('SMI')
# plt.grid(True)
# plt.show()
# ----------------------------------------------------------------------------------
# 
# lag_SMI = SMI_values.shift(1)
# diff_SMI = lag_SMI.diff()
# diff_DAX = DAX_values.diff()
# plt.figure(figsize=(8, 6))
# plt.scatter(diff_SMI, diff_DAX, color='skyblue', alpha=1)
# plt.title('Диаграмма разности между временными рядами SMI и DAX \n (со смещением SMI на один временной период вперед)')
# plt.xlabel('разность значений SMI с временным смещением')
# plt.ylabel('Разность значений DAX')
# plt.grid(True)
# plt.show()
# Как мы видим, корреляция исчезла после временного смещения
# ------------------------------------------------
cov_matrix = np.cov(DAX_values, SMI_values)
std_X = np.std(DAX_values)
std_Y = np.std(SMI_values)
corr_matrix = cov_matrix/(std_X*std_Y)


# Визуализация ковариационной матрицы
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', linewidths=0.5)
plt.title('Ковариационная матрица')
plt.xlabel('DAX                                      SMI')
plt.ylabel('SMI                                      DAX')
plt.show()
# Ковариационная матрица показывает тенденции между переменными, 
# а значения по одинаковым элементам это их дисперсия


