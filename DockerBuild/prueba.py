import sqlite3
import os

DB_DATA = 'data.db'

def clear_screen():
    os.system('clear') 

def pause():
    input("\nPress Enter to continue...")

def init_db():
    conn = sqlite3.connect(DB_DATA)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS PEOPLE
        (
            id INTEGER PRIMARY KEY,
            name TEXT(30) NOT NULL,
            lastname TEXT(50) NOT NULL,
            birthday TEXT NOT NULL
        )
    ''')
    
    cursor.execute("SELECT COUNT(*) FROM PEOPLE")
    if cursor.fetchone()[0] == 0:
        data_people = [
            (1, 'Martin', 'Castro', '1999-01-01'),
            (2, 'Nicolas', 'Muñoz', '2004-04-20'),
            (3, 'Fabian', 'Correa', '2004-08-28'),
            (4, 'Sofia', 'Gonzalez', '1995-05-15'),
            (5, 'Carlos', 'Rodriguez', '2001-11-30'),
            (6, 'Valentina', 'Gomez', '1998-07-22'),
            (7, 'Juan', 'Perez', '2003-02-10'),
            (8, 'Camila', 'Lopez', '2000-09-05'),
            (9, 'Andres', 'Martinez', '1997-03-12'),
            (10, 'Mariana', 'Sanchez', '2005-06-18'),
            (11, 'Sebastian', 'Ramirez', '1996-12-01'),
            (12, 'Isabella', 'Torres', '2002-10-25'),
            (13, 'David', 'Diaz', '1994-08-08')
        ]
        cursor.executemany("INSERT INTO PEOPLE VALUES (?, ?, ?, ?)", data_people)
        conn.commit()
    conn.close()

def show_people():
    clear_screen()
    conn = sqlite3.connect(DB_DATA)
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM PEOPLE ORDER BY name")
    PEOPLE = cursor.fetchall()
    
    if not PEOPLE:
        print("\nNo people registered in the database.")
    else:
        print(f"\n{'ID':<5}{'NAME':<30}{'LASTNAME':<50}{'BIRTHDAY':<15}")
        print("-" * 100)
        for persona in PEOPLE:
            print(f"{persona[0]:<5}{persona[1]:<30}{persona[2]:<50}{persona[3]:<15}")
    
    conn.close()
    pause() 

def locate_person():
    clear_screen()
    data_name = input("Name: ")
    
    conn = sqlite3.connect(DB_DATA)
    cursor = conn.cursor()
    
    query = "SELECT * FROM PEOPLE WHERE name LIKE ?"
    cursor.execute(query, ('%' + data_name + '%',))
    resultados = cursor.fetchall()
    
    print(f"--- PERSON: '{data_name}' ---")
    if not resultados:
        print(f"\nNot found PEOPLE with the name '{data_name}'.")
    else:
        print(f"\n{'ID':<5}{'NAME':<30}{'LASTNAME':<50}{'BIRTHDAY':<15}")
        print("-" * 100)
        for persona in resultados:
            print(f"{persona[0]:<5}{persona[1]:<30}{persona[2]:<50}{persona[3]:<15}")
    
    conn.close()
    pause()  

def main():
    init_db() 
    
    while True:
        clear_screen()
        print("\n--- MENU ---")
        print("1. PEOPLE")
        print("2. LOCATE")
        print("3. EXIT")
        
        option_select = input("\nSELECT OPTION: ")
        
        if option_select == '1':
            show_people()
        elif option_select == '2':
            locate_person()
        elif option_select == '3':
            break
        else:
            print("\nInvalid option.")

if __name__ == "__main__":
    main()