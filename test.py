import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()




def dfdfd():
    # Подключаемся к базе данных (если базы нет, она создастся)
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Создаем таблицу, если она не существует
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS test (
            id TEXT,
            napravlenie TEXT,
            lol TEXT
                    
        )
    ''')


    conn.commit()
    conn.close()


dfdfd()














