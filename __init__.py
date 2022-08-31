import requests
from getAssignmentDate import getAssignmentDueDate
from alert import *
from getAssignmentObjective import *
import time
from databaseManager import addUser
import sys
from datetime import date



# Fill in your details here to be posted to the login form.
payload = {
    'UserType': 'PARENTSWEB-STUDENT',
    'login': 'Log In'
}

def sendAllAlerts():

    users = []
    userDatabase = open('database/userLoginInfo.txt', 'r')
    count = 0
    for line in userDatabase:
        count+=1
        email = str(((line.split(' '))[1].split(' ')[0]))
        password = str(line.split(' ')[2])
        name = str(line.split(' ')[0])


        with requests.Session() as s:
            p = s.post('https://ec-va.client.renweb.com/pwr/', data=payload)

            r = s.get('https://ec-va.client.renweb.com/pwr/student/homework.cfm', data={'by': 'subject'})
            page = (r.text)


            #if int(input('Type "1" if you would like to save the page html code to text file. Type "2" to cancel: ')) == 1:
                #with open("PageHTML.txt", "w") as text_file:
                    #text_file.write(page)
                    #sys.exit()


            count = int(page.count('h3 class="pwr_card-heading alt">'))
            count1=0
            emailContextClasses=[]
            emailContext = 'You have assignments due tomorrow in these following classes. '
            classNames = '\n'

            for classText in range(count):
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

            #sys.exit()

        if emailContextClasses != None:
            classesDueTmr = int(len(emailContextClasses))
            for i in range(classesDueTmr):
                classNames = (classNames + emailContextClasses[i] + '\n')


            emailContext = ('Good evening ' + name + ',\n\n' + 'You have assignments due in the following classes. ' + classNames)
            #print(emailContext)
            #sys.exit()

        else:
            emailContext = ('Good evening ' + name + '!\n\n' + 'It\'s your lucky day! You have no assignments or tests due tomorrow!')




        sendEmail(emailContext, email)



# Automatic alert system loop
weekdayList = [1, 2, 3, 4, 5]
while True:
    currentHour = int(time.strftime("%H"))
    currentDay = int(date.today().isoweekday())
    #print(currentHour)
    print('Current hour = ' + str(currentHour))

    if currentDay in weekdayList:
        if currentHour == 18: # 6pm every day
            sendAllAlerts()
    
    time.sleep(55)
