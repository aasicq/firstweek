import sqlite3
conn = sqlite3.connect('database.db')
c = conn.cursor()

def create_table():
    """This method help you to create new table in a Database named user"""
    c.execute('CREATE TABLE IF NOT EXISTS user(id INTEGER PRIMARY KEY ASC, name TEXT, email VARCHAR(255), phone VARCHAR(14),bio TEXT,gender TEXT,DOB VARCHAR,address VARHCAR,longitude DOUBLE(9,6),latitude DOUBLE(9,6),photolink VARCHAR(255),sociallink VARCHAR(255))'
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
    
    

def read():
    c.execute('SELECT * FROM user')
    for row in c.fetchall():
        print(row)
        
def update():
    get_name = input("Enter New name: ")
    get_email = input("Enter your new email address: ")
    get_phonenumber = input("Update your phone: ")
    get_bio= input("Change your bio: ")
    get_DOB = input("Update your DOB: ")
    get_gender = input("Update your gender: ")
    get_address = input("Update  your address: ")
    get_longitude = float(input("Update your longitude: "))
    get_latitude = float(input("Update your latitude: "))
    get_photolink = input("Update your photolink: ")
    get_sociallink = input("Update your sociallink: ")
    get_id= int(input())
    
  
    c.execute(f"UPDATE user SET name='{get_name}', email='{get_email}',phone='{get_phonenumber}',\
        bio='{get_bio}', DOB='{get_DOB}', gender='{get_gender}', address='{get_address}',\
        longitude='{get_longitude}', latitude='{get_latitude}', photolink='{get_photolink}',\
        sociallink='{get_sociallink}' WHERE rowid={get_id}")
    
    for row in c.fetchall():
        print(row)
    
    conn.commit()
    

def delete():
    get_id = int(input("Enter id of user to delete: "))
    c.execute(f'DELETE FROM user where rowid={get_id}')
    conn.commit()
    



number = int(input("\
Enter the number \n\
1: Add user in User TABLE \n\
2: Read database \n\
3: Update the database \n\
4: Delete user from database\n\
"))
if number==1:
    create_row()
elif number==2:
    read()
elif number==3:
    update()
elif number==4:
    delete()
conn.close()