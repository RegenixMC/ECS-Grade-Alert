from dateManager import *
from bs4 import BeautifulSoup

def getAssignmentDueDate(classUnsortedText, allUnsortedText):

    if 'Assigned/Due:' in classUnsortedText:
        #date = ((classUnsortedText.split(':  '))[1].split(' ')[0])
        #month = int(date.split('/')[0])
        #year = getYearFromMonth(month)

        #return (date + '/' + str(year))

        allTextBeforeAssignment = allUnsortedText.split(classUnsortedText)[0]
        count = (int(allTextBeforeAssignment.count('<span class="pwr_date">')))
        
        date = ((allTextBeforeAssignment.split('<span class="pwr_date">'))[count].split('<')[0]) # Grabs the date from the header above the assignment
        return date



    elif 'Assigned:' in classUnsortedText:
        classUnsortedText = classUnsortedText.replace(' - HW', '', 1)
        date = ((classUnsortedText.split(' (Due:'))[1].split(')')[0])

        return (date)



    elif 'Due:' in classUnsortedText:
        classUnsortedText = classUnsortedText.replace(' - HW', '', 1)
        date = ((classUnsortedText.split('Due:  '))[1].split(':')[0])
        month = (date.split('/')[0])
        if month.isdigit() == True:
            year = getYearFromMonth(month)

            return (date + '/' + str(year))
        else:
            allTextBeforeAssignment = allUnsortedText.split(classUnsortedText)[0]
            count = (int(allTextBeforeAssignment.count('<span class="pwr_date">')))
            
            date = ((allTextBeforeAssignment.split('<span class="pwr_date">'))[count].split('<')[0]) # Grabs the date from the header above the assignment
            return date
            



    else:
        allTextBeforeAssignment = allUnsortedText.split(classUnsortedText)[0]
        count = (int(allTextBeforeAssignment.count('<span class="pwr_date">')))
        
        date = ((allTextBeforeAssignment.split('<span class="pwr_date">'))[count].split('<')[0]) # Grabs the date from the header above the assignment
        return date