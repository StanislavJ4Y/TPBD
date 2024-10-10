import sqlite3

# Підключаємося до бази даних або створюємо файл, якщо його немає)
conn = sqlite3.connect('income_expense.db')
cursor = conn.cursor()

# Створення таблиць (реалізація бази даних завдання 1)
cursor.execute('''
CREATE TABLE IF NOT EXISTS People (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    middle_name TEXT,
    phone_number TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS PaymentMethod (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    method TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Income (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    person_id INTEGER,
    work_place TEXT,
    position TEXT,
    income_source TEXT,
    card_number TEXT,
    amount REAL,
    date_received TEXT,
    FOREIGN KEY (person_id) REFERENCES People(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    person_id INTEGER,
    payment_method_id INTEGER,
    description TEXT,
    amount REAL,
    date_expended TEXT,
    transaction_time TEXT,
    location TEXT,
    address TEXT,
    FOREIGN KEY (person_id) REFERENCES People(id),
    FOREIGN KEY (payment_method_id) REFERENCES PaymentMethod(id)
)
''')

# Початкові дані (завдання 2: Наповнити базу даних інформацією)
cursor.execute('INSERT INTO People (first_name, last_name, middle_name, phone_number) VALUES (?, ?, ?, ?)',
               ('Стас', 'Палагній', 'Олегович', '380962116552'))

cursor.execute('INSERT INTO PaymentMethod (method) VALUES (?)', ('готівка',))
cursor.execute('INSERT INTO PaymentMethod (method) VALUES (?)', ('карта',))

cursor.execute('INSERT INTO Income (person_id, work_place, position, income_source, card_number, amount, date_received) VALUES (?, ?, ?, ?, ?, ?, ?)',
               (1, 'ТОВ Нова Пошта', 'фахівець оператор', 'зарплата', '1234-5678-9012-3456', 17800, '2024-10-01'))

cursor.execute('INSERT INTO Expenses (person_id, payment_method_id, description, amount, date_expended, transaction_time, location, address) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
               (1, 2, 'Купівля ноутбука', 250000, '2024-10-05', '12:30', 'Магазин', 'м. Київ, вул. Соломʼянська, 7'))

conn.commit()  # Зберігаємо зміни
conn.close()  # Закриваємо підключення