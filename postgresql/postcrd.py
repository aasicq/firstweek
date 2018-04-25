import psycopg2
import json

conn = psycopg2.connect("dbname=student user=postgres password=aashiq123")
c = conn.cursor()


def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS students(id SERIAL PRIMARY KEY, name TEXT, age INT, address TEXT)")
    conn.commit()

def insert_content():
    raw = json.load(open('/home/aashiq/Desktop/firstweek/postgresql/dat.json'))
    for i in raw:
        c.execute(f"INSERT INTO students(age, name, address) VALUES ({i['age']}, '{i['name']}', '{i['address']}')")        
        conn.commit()
    
    
create_table()
insert_content()
c.close()
conn.close()