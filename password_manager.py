from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file: #Open file called key.key and write in bytes
        key_file.write(key) '''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def view():
    print("\nPasswords:")
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, view_pass = data.split("|")
            print("User:", user, "  Password:", 
                fer.decrypt(view_pass.encode()).decode())

def add():
    name = input("Account name: ")
    pwd = input("Password: ")
    #with keyword closes file after use
    with open('passwords.txt', 'a') as f:
        f.write(name + " | " + fer.encrypt(pwd.encode()).decode() + "\n")

menu = True
while menu == True:
    mode = input("Would you like to add a new password or view existing ones? \n"
                "1. View\n"
                "2. Add\n"
                "3. Quit\n"
                "Option: ")
    if mode == "1":
        view()
    elif mode == "2":
        add()
    elif mode == "3":
        menu = False
    else:
        print("Invalid input.")
