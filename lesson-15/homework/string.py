# 1
import sqlite3

with sqlite3.connect('homew.db') as conn:
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Roster (
            Name TEXT,
            Species TEXT,
            Age INTEGER
        )
    ''')
    
    conn.commit()
# 2
with sqlite3.connect('homew.db') as conn:
    cursor = conn.cursor()
    data = [('Benjamin Sisko', 'Human', 40),
            ('Jadzia Dax', 'Trill', 300),
            ('Kira Nerys', 'Bajoran', 29)]
    cursor.executemany("INSERT INTO Roster VALUES (?, ?, ?)", data)
    conn.commit()
  # 3
with sqlite3.connect('homew.db') as conn:
    cursor = conn.cursor()
    updata="""UPDATE roster 
            set name ='Ezri Dax'
            where name ='Jadzia Dax'"""
    cursor.execute(updata)
    conn.commit()
  # 4
import sqlite3

with sqlite3.connect('homew.db') as conn:
    cursor = conn.cursor()
    
    query = """SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'"""
    cursor.execute(query)
    
    results = cursor.fetchall()  

    for row in results:
        print(row)  
