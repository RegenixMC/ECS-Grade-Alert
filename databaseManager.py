import sys

def addUser(username, email, password):
    with open("database/user_database.json", "a") as database:
        database.write(username + ' ' + email + ' ' + password + '\n')
    return 2

    
while True:
    while True:
        code = 0
        username = str(input('Enter FACTS username: '))
        password = str(input('Enter FACTS password: '))
        email = str(input('Enter email: '))
        if ' ' in username:
            username = username.replace(' ', '_')
            code = 2
        if ' ' in email:
            print("Can't have spaces in the email!\n---------------------------------------------")
            code = 1
        if ' ' in password:
            print("Can't have spaces in the password!\n---------------------------------------------")
            code = 1

        if code == 1:
            pass
        else:
            break
        
        
        

        
    userSubmit = addUser(username, email, password)
    if userSubmit == 2:
        print('User added!')
    
    if int(input('Type 1 to add a new user, type 2 to end program: ')) == 2:
        break
    print('---------------------------------------------')