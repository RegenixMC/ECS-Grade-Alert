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
        calendar = (s.post('https://ec-va.client.renweb.com/pwr/school/'))
        calendar = calendar.text

        currentYear = date.today().strftime("%y")
        currentMonth = (date.today().strftime("%m")).replace('0', '')
        currentDay = (int(date.today().strftime("%d")) + 1)

        allTextAfterDate = calendar.split(str(currentMonth) + '/' + str(currentDay) + '/' + str(currentYear))[1]
        dayColorDate = str((allTextAfterDate.split('<h5>'))[1].split('</h5>')[0]).replace(' ', '').lower() # Grabs the raw text from the header above the current day on the calendar
        if 'white' in dayColorDate:
            return 'White'
        elif 'blue' in dayColorDate:
            return 'Blue'

        else:
            print('ERROR! This error could have been caused by FACTS updating their website html.')
            return 'NONE'