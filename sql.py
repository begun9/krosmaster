import sqlite3

conn = sqlite3.connect('testdb.db')
cursor = conn.cursor()
row = cursor.execute("select name from sqlite_master where type = 'table' and name = 'heroes'").fetchone()
try: # Проверка на наличите таблицы
    if row[0] != 'heroes':
        cursor.execute("""CREATE TABLE heroes
                      (name text, level int, dam int,
                       deff int, item text)
                   """)
except TypeError:
    cursor.execute("""CREATE TABLE heroes
                         (name text, level int, dam int,
                          deff int, item text)
                      """)
# for row in cursor.execute("select name from sqlite_master where type = 'table'"):
#     # if row == 'heroes':
#         print(row[0])

row = cursor.execute("select name from sqlite_master where type = 'table' and name = 'heroes'").fetchone()
# row = cursor.fetchone()
print(row[0])