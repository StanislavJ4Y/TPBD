import sqlite3

#(Завдання 3: Відображення даних таблиць)
def display_table_data():
    conn = sqlite3.connect('income_expense.db')
    cursor = conn.cursor()

    # Вибір всіх даних із таблиці люди
    cursor.execute('SELECT * FROM People')
    people = cursor.fetchall()

    print("people:")
    for person in people:
        print(person)

    # Вибір всіх даних із таблиці прибуток
    cursor.execute('SELECT * FROM Income')
    income = cursor.fetchall()

    print("\nIncome:")
    for inc in income:
        print(inc)


    cursor.execute('SELECT * FROM Expenses')
    expenses = cursor.fetchall()

    print("\nExpenses:")
    for exp in expenses:
        print(exp)

    conn.close()

# Виклик функції для відображення даних
display_table_data()


#(Завдання 4: Додавання рядків у таблицю)
def add_person(first_name, last_name, middle_name, phone_number):
    conn = sqlite3.connect('income_expense.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO People (first_name, last_name, middle_name, phone_number) VALUES (?, ?, ?, ?)',
                   (first_name, last_name, middle_name, phone_number))
    conn.commit()
    conn.close()


# Виклик функції для додавання нового запису
add_person('Олександр', 'Слєпченко', 'Романович', '380669922649')

display_table_data()

def join_query():
    conn = sqlite3.connect('income_expense.db')
    cursor = conn.cursor()

    # Витрати з інформацією про користувача
    cursor.execute('''
    SELECT People.first_name, People.last_name, Expenses.description, Expenses.amount 
    FROM Expenses 
    JOIN People ON Expenses.person_id = People.id
    ''')

    result = cursor.fetchall()

    print("\nExpenses with users:")
    for row in result:
        print(row)

    conn.close()


# Виклик функції для виконання JOIN-запиту
join_query()


def filter_query():
    conn = sqlite3.connect('income_expense.db')
    cursor = conn.cursor()

    # Витрати, де сума більше 10000
    cursor.execute('SELECT * FROM Expenses WHERE amount > 10000')
    result = cursor.fetchall()

    print("\nВитрати, де сума більше 10000:")
    for row in result:
        print(row)

    conn.close()

# Виклик функції для виконання запиту з фільтрацією
filter_query()


def aggregate_query():
    conn = sqlite3.connect('income_expense.db')
    cursor = conn.cursor()

    # Загальна сума витрат
    cursor.execute('SELECT SUM(amount) FROM Expenses')
    total_expenses = cursor.fetchone()[0]

    print(f"\nTotal amount of expenses: {total_expenses} grn")

    conn.close()

# Виклик функції для виконання агрегатного запиту
aggregate_query()



