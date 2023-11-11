import sqlite3

db = sqlite3.connect('server.db')

sql = db.cursor()

sql.execute('''CREATE TABLE IF NOT EXISTS tab_text_1 (Login TEXT, Pasvord INTEGER, Email TEXT)''')
db.commit()

user_login = input('Логин:')
sql.execute("INSERT INTO tab_text_1(Login) VALUES (?)", (user_login,))

user_pasvord = input('Пароль котороый состоит только из цифр :')
sql.execute("INSERT INTO tab_text_1(Pasvord) VALUES (?)", (user_pasvord,))

user_email = input('E-mail:')
sql.execute("INSERT INTO tab_text_1(Email) VALUES (?)", (user_email,))
db.commit()

sql.close()
db.close()
