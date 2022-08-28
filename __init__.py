import requests
from getAssignmentDate import getAssignmentStatus



# Fill in your details here to be posted to the login form.
payload = {
    'UserType': 'PARENTSWEB-STUDENT',
    'login': 'Log In'
}

payload['username'] = 'Evan Britton'
payload['password'] = 'Spa#12950715'
payload['DistrictCode'] = 'EC-VA'


with requests.Session() as s:
    p = s.post('https://ec-va.client.renweb.com/pwr/', data=payload)
    #print (p.text)

    r = s.get('https://ec-va.client.renweb.com/pwr/student/homework.cfm', data={'by': 'subject'})
    page = (r.text)
    #print(page)
    count = int(page.count('h3 class="pwr_card-heading alt">'))
    #count = 1
    count1 = 0
    for classText in range(count):
        count1+=1
        classUnsortedText = ((page.split('h3 class="pwr_card-heading alt"'))[count1].split('</div>')[0])

        className = ((classUnsortedText.split('>'))[1].split('<')[0])
        classAssignmentStatus = getAssignmentStatus(classUnsortedText, page)




        #print(classUnsortedText)
        print(className, classAssignmentStatus)