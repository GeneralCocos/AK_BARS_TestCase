import pandas as pd

df = pd.read_csv('clients.csv')

# 1. Количество неактивных клиентов с балансом > 100000
inactive_rich = df[(df['is_active'] == 0) & (df['balance'] > 100000)]
print("1. Количество неактивных клиентов с балансом > 100000:", len(inactive_rich))

# 2. Средний кредитный рейтинг по странам
avg_credit_by_country = df.groupby('country')['credit_score'].mean()
print("\n2. Средний кредитный рейтинг по странам:\n", avg_credit_by_country)

# 3. Процент ушедших клиентов в разрезе типов карт
left_by_card = df.groupby('card_type')['left_company'].mean() * 100
print("\n3. Процент ушедших по типам карт:\n", left_by_card)

# 4. Сравнение зарплаты клиента со средней зарплатой по стране
df['avg_salary_by_country'] = df.groupby('country')['salary'].transform('mean')
df['salary_cmp'] = df['salary'] - df['avg_salary_by_country']
print("\n4. Примеры сравнения зарплаты клиента со средней по стране:\n", df[[
      'id', 'country', 'salary', 'avg_salary_by_country', 'salary_cmp']].head())

# 5. Страны, в которых в топ-10 зарплат больше женщин, чем мужчин
top10 = df.sort_values(
    by='salary', ascending=False).groupby('country').head(10)
gender_counts = top10.groupby(
    ['country', 'gender']).size().unstack(fill_value=0)
more_women_top = gender_counts[gender_counts['Female'] > gender_counts['Male']]
print("\n5. Страны, где в топ-10 по зарплате больше женщин:\n",
      more_women_top.index.tolist())

# 6. Страны, в которых используются не все типы карт
all_card_types = set(df['card_type'].unique())
card_types_by_country = df.groupby(
    'country')['card_type'].apply(lambda x: set(x))
not_all_types = card_types_by_country[card_types_by_country.apply(
    lambda x: x != all_card_types)]
print("\n6. Страны, где не все типы карт используются:\n",
      not_all_types.index.tolist())

# Количество клиентов со страницы "датасет - Клиенты"
print("\nКоличество клиентов:", len(df))
