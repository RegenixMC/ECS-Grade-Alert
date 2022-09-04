from sendAllAlerts import *
import time
from getAssignmentDate import *
from getCalendarDay import *
from alert import *
from dateManager import *



#sendAllAlerts()

# Automatic alert system loop
weekdayList = [7, 1, 2, 3, 4]
while True:
    currentHour = int(time.strftime("%H"))
    currentDay = int(date.today().isoweekday())
    print(currentDay)

    if currentDay in weekdayList:
        print('Current hour = ' + str(currentHour))
        sendHour = 15  # 18 = 6pm every day
        if currentHour == sendHour:
            print('Sending alerts...')
            sendAllAlerts()
            time.sleep(3600)
    time.sleep(10)
