import sqlite3

# Функция для создания базы данных и таблицы
def create():
    # Подключаемся к базе данных (если базы нет, она создастся)
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Создаем таблицу, если она не существует
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS test (
            nap TEXT,
            "1v" BOOLEAN,
            "2v" BOOLEAN,
            "3v" BOOLEAN,
            "4v" BOOLEAN,
            "5v" BOOLEAN,
            "6v" BOOLEAN,
            "7v" BOOLEAN,
            "8v" BOOLEAN,
            "9v" BOOLEAN,
            "10v" BOOLEAN,
            "11v" BOOLEAN,
            "12v" BOOLEAN,
            "13v" BOOLEAN,
            "14v" BOOLEAN,
            "15v" BOOLEAN     
        )
    ''')

    conn.commit()
    conn.close()

def dfdfd():
    # Подключаемся к базе данных (если базы нет, она создастся)
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Создаем таблицу, если она не существует
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vyz (
            vyz_sokr TEXT,
            napravlenie TEXT,
            gorod TEXT,
            site TEXT,
            prbb TEXT,
            prbp TEXT,
            Polnoe TEXT
                     
        )
    ''')


    conn.commit()
    conn.close()


dfdfd()



























# Функция для создания базы данных и таблицы
def create_db():
    # Подключаемся к базе данных (если базы нет, она создастся)
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Создаем таблицу, если она не существует
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            napravlenie TEXT         
        )
    ''')

    


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS directions (
            code TEXT PRIMARY KEY,
            name TEXT
        )
    ''')

# Добавление направлений
    cursor.execute("INSERT OR IGNORE INTO directions (code, name) VALUES ('F1', 'Физика')")
    cursor.execute("INSERT OR IGNORE INTO directions (code, name) VALUES ('F2', 'Математика')")
    cursor.execute("INSERT OR IGNORE INTO directions (code, name) VALUES ('G1', 'География')")
    cursor.execute("INSERT OR IGNORE INTO directions (code, name) VALUES ('H1', 'История')")
    



    
    # Закрываем соединение с базой данных
    conn.commit()
    conn.close()

# Вызовем функцию для создания базы данных и таблицы
create_db()

conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS professions_test (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nap TEXT,
        "1v" BOOLEAN,
        "2v" BOOLEAN,
        "3v" BOOLEAN,
        "4v" BOOLEAN,
        "5v" BOOLEAN,
        "6v" BOOLEAN,
        "7v" BOOLEAN,
        "8v" BOOLEAN,
        "9v" BOOLEAN,
        "10v" BOOLEAN,
        "11v" BOOLEAN,
        "12v" BOOLEAN,
        "13v" BOOLEAN,
        "14v" BOOLEAN,
        "15v" BOOLEAN
    )
''')

# Пример добавления направлений с ответами (True/False для каждой профессии)
directions_and_answers = [
    ("Инженер", True, True, False, False, False, False, True, False, True, False, False, False, False, False),
    ("IT-специалист", True, True, False, False, False, False, True, False, True, False, False, False, False, False),
    ("Маркетолог", False, False, True, False, True, False, False, True, False, True, False, False, True, True),
    ("Химик", False, False, False, True, False, True, False, False, False, False, True, False, False, False),
    ("Экономист", False, False, False, False, True, False, False, True, False, False, True, False, False, True),
    ("Ботаник", False, False, False, False, False, True, False, True, False, False, True, False, False, False),
    ("Аллерголог", False, False, False, False, False, False, True, False, False, False, True, False, False, False),
    ("Психотерапевт", True, False, False, True, False, False, False, True, False, True, True, False, False, True),
    ("Эколог", False, False, False, False, False, False, False, False, True, False, False, False, False, True),
    ("Психолог", True, False, False, False, False, False, False, True, False, True, True, False, False, True),
    ("Преподаватель", False, False, False, False, True, False, True, True, False, False, True, False, True, True),
    ("Журналист", False, True, True, False, False, False, True, False, False, False, True, False, False, False),
    ("Адвокат", False, False, False, False, False, False, True, True, False, False, False, True, True, True),
    ("Бухгалтер", False, False, False, False, True, False, False, True, False, True, False, False, True, True),
    ("Финансист", False, False, True, False, True, False, False, True, False, False, True, False, False, True),
]

# Вставка данных направлений и их ответов (не добавляем "id", так как он автоинкрементируется)
cursor.executemany('''
    INSERT INTO professions_test (nap, "1v", "2v", "3v", "4v", "5v", "6v", "7v", "8v", "9v", "10v", "11v", "12v", "13v", "14v", "15v")
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', directions_and_answers)

conn.commit()

# Закрытие соединения
conn.close()

# Сохранение изменений и закрытие соединения
conn.commit()

# Закрытие соединения
conn.close()