def getAssignmentStatus(classUnsortedText, allUnsortedText):

    if 'Assigned/Due:' in classUnsortedText:
        return 'Assigned/Due'
    elif 'Assigned:' in classUnsortedText:
        return 'Assigned'
    elif 'Due:' in classUnsortedText:
        return 'Due'
    else:
        allTextBeforeAssignment = allUnsortedText.split(classUnsortedText)[0]
        count = (int(allTextBeforeAssignment.count('<span class="pwr_date">')))
        
        date = ((allTextBeforeAssignment.split('<span class="pwr_date">'))[count].split('<')[0])
        return (date)
