import json

def save_data_to_json(data):
    with open('users.json', 'w') as file:
        json.dump(data, file)

def load_data_from_json():
    with open('users.json', 'r') as file:
        data = json.load(file) 
    return data

def create_user(data):
    username = input("Enter username: ")

    for user in data:
        if user["username"] == username:
            print("This username is already exist.")
            return
    password = input("Enter password: ")
    if len(password) < 8:
        print("Your password is less than 8.")
        return 
    user = {"username": username, "password": password}
    data.append(user)
    save_data_to_json(data)
    print("User registered successfully.")

def read_user(data):
    username = input("Enter username to search: ")
    for user in data:
        if user["username"] == username:
            print(user)
            return
    print("User not found.")

def update_user(data):
    username = input("Enter username to update: ")
    new_password = input("Enter new password: ")
    for user in data:
        if user["username"] == username:
            user["password"] = new_password
            save_data_to_json(data)
            print("User updated.")
            return
    print("User not found.")

def delete_user(data):
    username = input("Enter username to delete: ")
    for user in data:
        if user["username"] == username:
            data.remove(user)
            save_data_to_json(data)
            print("User deleted.")
            return
    print("User not found.")
users_data = load_data_from_json()

while True:
    print("Menu:")
    print("1. Create User")
    print("2. Read User")
    print("3. Update User")
    print("4. Delete User")
    print("5. Exit")
    choice = input("choice: ")
    if choice == "1":
        create_user(users_data)
    elif choice == "2":
        read_user(users_data)
    elif choice == "3":
        update_user(users_data)
    elif choice == "4":
        delete_user(users_data)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Error!")