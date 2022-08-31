def addUser(userName, loginEmail, loginPassword):
    if ' ' in userName or ' ' in userName:
        return 1
    if ' ' in loginEmail or ' ' in loginEmail:
        return 1
    if ' ' in loginPassword or ' ' in loginPassword:
        return 1

    with open("database/userLoginInfo.txt", "a") as text_file:
        text_file.write(userName + ' ' + loginEmail + ' ' + loginPassword + '\n')
        return 2

#addUser('Derek', 'derek.m.britton@gmail.com', 'Spa#1295')