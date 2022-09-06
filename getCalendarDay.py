import requests
from datetime import date
import sys

userDatabase = open('database/user_database.json', 'r')

def getDayColor(username, password):

    payload = {
                'UserType': 'PARENTSWEB-STUDENT',
                'login': 'Log In',
                'DistrictCode': 'EC-VA',
                'username': username,
                'password': password
            }



    with requests.Session() as s:
        calendar = s.post('https://ec-va.client.renweb.com/pwr/', data=payload)
        calendar = (s.post('https://ec-va.client.renweb.com/pwr/school/')).text

        currentYear = date.today().strftime("%y")
        currentMonth = (date.today().strftime("%m")).replace('0', '')
        currentDay = (int(date.today().strftime("%d"))) + 1
        tmrDate = str(currentMonth) + '/' + str(currentDay) + '/' + str(currentYear)

        dateCount = calendar.count(tmrDate)

        #with open("2PageHTML.txt", "w") as text_file:
            #text_file.write(calendar)
            
        count1 = 0
        for i in range(dateCount):
            count1 +=1
            try:
                dateCheck = ((calendar.split(tmrDate))[count1].split('</tr>')[0]).lower()
                if 'white' in dateCheck:
                    return 'White'
                elif 'blue' in dateCheck:
                    return 'Blue'
            except:
                pass
        

        return 'failed'
        # Maybe no school this day? or website html changed and code has to be updated