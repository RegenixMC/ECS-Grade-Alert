def getAssignmentStatus(classUnsortedText, allUnsortedText):

    if 'Assigned/Due:' in classUnsortedText:
        return 'Assigned/Due'
    elif 'Assigned:' in classUnsortedText:
        return 'Assigned'
    elif 'Due:' in classUnsortedText:
        return 'Due'
    else:
        classUnsortedText = ((page.split('h3 class="pwr_card-heading alt"'))[count1].split('</div>')[0])
        return 'Due'