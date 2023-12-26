import pandas as pd
import xml.etree.ElementTree as ET

df = pd.read_csv('books.csv', delimiter=';', encoding='cp1251')
long_title_count = len(df[df['Название'].str.len() > 30])
print(f'Количество записей с названием длиннее 30 символов: {long_title_count}')

print('введите ФИО автора')
name=input()
name=str(name)

filtered_books = df[(df['Автор (ФИО)'] == name) & (pd.to_datetime(df['Дата поступления'], format='%d.%m.%Y %H:%M').dt.year < 2016)]
print(filtered_books)

random_books = df.sample(20)
with open('bibliography.txt', 'w', encoding='cp1251') as file:
    for index, row in random_books.iterrows():
        bibliography = f"{row['Автор (ФИО)']} ({row['Автор']}). {row['Название']} - {row['Дата поступления']}\n"
        file.write(bibliography)

tree = ET.parse('currency.xml')
root = tree.getroot()

currency_data = []
for child in root:
    name = child.find('Name').text
    value = float(child.find('Value').text.replace(',', '.'))
    currency_data.append({'Name': name, 'Value': value})

currency_df = pd.DataFrame(currency_data)
print(currency_df)
