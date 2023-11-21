master_pwd = input("What is the master password? ")
menu = True

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, view_pass = data.split("|")
            print("User:", user, "\nPassword:", view_pass)

def add():
    name = input("Account name: ")
    pwd = input("Password: ")
    #with keyword closes file after use
    with open("passwords.txt, ", "a") as f:
        f.write(name + "|" + pwd + "\n")


while menu == True:
    mode = input("Would you like to add a new password or view existing ones? \n"
                "1. View\n"
                "2. Add\n")
    if mode == "1":
            pass
    elif mode == "2":
        pass
    else:
        print("Invalid input.")
