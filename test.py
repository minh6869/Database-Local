import sqlite3

connect = sqlite3.connect("local.sqlite")
cursor = connect.cursor()
cursor.execute('''
               CREATE TABLE IF NOT EXISTS test(
               id INTERGER PRIMARY KEY
               )
               ''')
connect.commit()
cursor.execute('''
            INSERT INTO test(id)  VALUES(1)
''')
connect.commit()
cursor.execute('''
            SELECT * FROM test    
''')
result = cursor.fetchall()
print(result)