import requests
from getAssignmentDate import getAssignmentDueDate
from alert import *
import sys
from datetime import date
from getCalendarDay import *



def sendAllAlerts():

    userDatabase = open('database/user_database.json', 'r')
    for line in userDatabase:
        username = str(line.split(' ')[0]).replace('_', ' ')
        email = str(line.split(' ')[1].split(' ')[0])
        password = (str(line.split(' ')[2]))
        #print(username, email, password) # log the user information for testing purposes


        payload = {
            'UserType': 'PARENTSWEB-STUDENT',
            'login': 'Log In',
            'DistrictCode': 'EC-VA',
            'username': username,
            'password': password
        }


        with requests.Session() as s:
            page = s.post('https://ec-va.client.renweb.com/pwr/', data=payload)
            page = (s.get('https://ec-va.client.renweb.com/pwr/student/homework.cfm')).text


            #if int(input('Type "1" if you would like to save the page html code to text file. Type "2" to cancel: ')) == 1:
                #with open("PageHTML.txt", "w") as text_file:
                    #text_file.write(page)


            count = int(page.count('h3 class="pwr_card-heading alt">'))
            count1=0
            emailContextClasses=[]
            userName = ((page.split('<div class="pwr_user-name">'))[1].split('</div>')[0])
            classNames = '\n'

            for i in range(count):
                count1+=1
                classUnsortedText = ((page.split('h3 class="pwr_card-heading alt"'))[count1].split('</div>')[0])

                assignmentName = ((classUnsortedText.split('>'))[1].split('<')[0])
                assignmentDueDate = getAssignmentDueDate(classUnsortedText, page)

                currentYear = date.today().strftime("%Y")
                currentMonth = (date.today().strftime("%m")).replace('0', '')
                currentDay = (int(date.today().strftime("%d")) + 1)
                tmr = str(str(currentMonth) + '/' + str(currentDay) + '/' + str(currentYear))

                if tmr == assignmentDueDate:
                    emailContextClasses.append(assignmentName)
                #print(assignmentName + ' ' + assignmentDueDate)



        emailContext = ('Good evening ' + userName + ',\n\n' + 'Tomorrow will be a ' + getDayColor(username, password) + ' Day so make make sure you have the required notebooks and folders for your classes.\n')
        
        if emailContextClasses != []:
            classesDueTmr = int(len(emailContextClasses))
            for i in range(classesDueTmr):
                classNames = (classNames + emailContextClasses[i] + '\n')

            emailContext = ('Good evening ' + userName + ',\n\n' + 'Tomorrow will be a ' + getDayColor(username, password) + ' Day so make make sure you have the required notebooks and folders.\n' + 'You have an assignment and/or a test due tomorrow in the following classes...' + classNames)

        else:
            emailContext = ('Good evening ' + userName + ',\n\n' + 'Tomorrow will be a ' + getDayColor(username, password) + ' Day so make make sure you have the required notebooks and folders.\n' + 'It\'s your lucky day! You have no assignments or tests due tomorrow!')




        sendEmail(emailContext, email)