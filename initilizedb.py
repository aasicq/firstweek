import sqlite3
conn = sqlite3.connect('database.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS user(name TEXT, email VARCHAR(255), phone VARCHAR(14),bio TEXT,gender TEXT,DOB VARCHAR,address VARHCAR,longitude DOUBLE(9,6),latitude DOUBLE(9,6),photolink VARCHAR(255),sociallink VARCHAR(255))'
)

def create_row():
    for i in range(2):

        sql = ''' INSERT INTO user(name, email, phone, bio, gender, DOB, address, longitude, latitude, photolink, sociallink)
                VALUES(?,?,?,?,?,?,?,?,?,?,?)'''
        
        data = [
            
                (input("Enter your name: ")),
                (input("Enter your Email: ")),
                (input("Enter your phone number: ")),
                (input("Say something about you: ")),
                (input("Enter your DOB: ")),
                (input("Your Gender: ")),
                (input("Enter your Address: ")),
                (float(input("Enter your address longitude: "))),
                (float(input("Enter your address latitude: "))),
                (input("Enter your photolink: ")),
                (input("Enter your socialLink: "))
                
        ]

    c.execute(sql, data)
    conn.commit()
    conn.close()

def read():
    c.execute('SELECT * FROM user')
    for row in c.fetchall():
        print(row)
        
def update():
    getvar = input()
    getnum = float(input())
    c.execute('SELECT * FROM user')
    for row in c.fetchall():
        print(row)
    
    
create_table()
read()
update()