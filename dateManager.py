from datetime import date

def getYearFromMonth(month):
    currentYear = date.today().strftime("%Y")
    currentMonth = (date.today().strftime("%m")).replace('0', '')

    if (int(month)) < int(currentMonth)-2:
        year = int(currentYear) + 1
        return year
    else:
        year = currentYear
        return year