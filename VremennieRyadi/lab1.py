import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller

# Создаем dataset с данными о продажах
data = {'Дата': ['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01', '2023-05-01'],
        'Продажи': [1000, 1200, 1300, 1100, 1400]}

df = pd.DataFrame(data)

# Преобразуем столбец 'Дата' в формат даты
df['Дата'] = pd.to_datetime(df['Дата'])

# Построим график продаж
plt.plot(df['Дата'], df['Продажи'])
plt.title('Продажи в магазине МВидео')
plt.xlabel('Дата')
plt.ylabel('Продажи')
plt.show()

# Проведем тест Дики-Фуллера на стационарность
result = adfuller(df['Продажи'])

print('ADF Statistic: %f' % result[0])
print('p-value: %f' % result[1])
print('Critical Values:')
for key, value in result[4].items():
    print('\t%s: %.3f' % (key, value))