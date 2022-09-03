from sendAllAlerts import *
import time
from getAssignmentDate import *
from getCalendarDay import *
from alert import *
from dateManager import *



#sendAllAlerts()

# Automatic alert system loop
weekdayList = [1, 2, 3, 4, 5]
while True:
    currentHour = int(time.strftime("%H"))
    currentDay = int(date.today().isoweekday())
    print('Current hour = ' + str(currentHour))

    if currentDay in weekdayList:
        sendHour = 18  # 6pm every day
        if currentHour == sendHour:
            sendAllAlerts()
            while True:
                if currentHour == sendHour + 1:
                    break
    time.sleep(60)
