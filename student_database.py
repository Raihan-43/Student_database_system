import json
from tabulate import tabulate


def display_choice():
    print("1. Add Student")
    print("2. Show all the students")
    print("3. Delete an entry")
    print("4. Search student")
    print("5. Exit the program")

def load_previous_data():
    with open('database.json', 'r') as file:
        try:
            return json.load(file)
            # print(database)
        except FileNotFoundError:
            return []
            print("\nFile not found in the directory\n")
        except json.JSONDecodeError:
            return []
            print("\nThe json file is corrupted\n")
            


def add_new_student():
    name = input("Enter name: ")
    age= input("Enter age: ")
    city = input("Enter city: ")
    try:
        age= int(age)
    except ValueError:
        print("\nEnter only number for age\n")
    else:
        student= {'name': name, 'age': age, 'city': city}
        database.append(student)

def delete_student(serial_no):
    del database[serial_no-1]
    print(f"\nStudent with serial no {serial_no} is deleted successfully\n ")

def save_data():
    with open('database.json', 'w') as file:
        json.dump(database, file, indent= 4)

def show_database(data_base):
    print("-"*50)
    print("Showing database")
    print("-"*50)
    # print(database)
    print(tabulate(data_base, headers= 'keys', tablefmt= 'grid'))

def search_student():
    print("1. Search by Name")
    print("2. Search by City")
    print("3. Search by Age")
    search= input("Select one: ")

    if search=='1':
        searched_name= input("Enter the name of the student that you want to find: ")
        data_name= [item for item in database if item['name']== searched_name]
        show_database(data_name)
    elif search== '2':
        searched_city= input("Enter the City of the student that you want to find: ")
        data_city= [item for item in database if item['city']== searched_city]
        show_database(data_city)
    
    elif search== '3':
        searched_age= input("Enter the Age of the student that you want to find: ")
        data_age= [item for item in database if item['age']== searched_age]
        show_database(data_age)
    else:
        print("\nPlease select a valid number\n")


    
# database = [] #list of dictionaries

while True:
    database= load_previous_data()
    display_choice()
    mode= input("Select your choice: ")
    if mode == '1':
        add_new_student()
        save_data()
    
    elif mode=='2':
        show_database(database)
    
    elif mode == '3':
        serial= int(input("Enter serial: "))
        delete_student(serial)
        save_data()
    
    elif mode == '5':
        break

    elif mode =='4':
        search_student()
    
    else:
        print("\nPlease select a valid number\n")