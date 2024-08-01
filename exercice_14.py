def isLeap(a):
    """
    This function verifies if a year i leap
    """
    if a % 4 == 0:
        if a % 100 == 0:
            if a % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def verifyDate(n):
    """
    This function verifies if a date is correct, written as DDMMAAAA
    """
    day = n[0:2]
    month = n[2:4]
    year = n[4:8]

    if len(n) != 8:
        return False
    else:
        if 1 <= int(day) <= 31:
            if 1 <= int(month) <= 12:
                if int(day) == 31:
                    if month in ['01', '03', '05', '07', '08', '10', '12']:
                        return True
                    else:
                        return False
                elif int(month) == 2:
                    if 30 <= int(day):
                        return False
                    elif int(day) == 29:
                        return isLeap(int(year))
                    else:
                        return True
                else:
                    return True
            else:
                return False
        else:
            return False

def isInt(n):
    """
    This function verifies if n is an integer or not
    """
    try:
        int(n)
        return True
    except ValueError:
        return False
    
def whichDate(n):
    day = int(n[0:2])
    month = int(n[2:4])
    year = int(n[4:8])
    x = 0
    y = 0
    exp = 0

    if (month == 1) or (month == 2):
        x = year - 1
        y = month + 12
    else:
        x = year
        y = month
    exp = day - 1 + (5 * x // 4) - (x // 100) + (x // 400) + (13 * (y + 1) // 5)
    final = exp % 7
    dic = {0:'Sunday', 1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday'}
    return dic[final]

val = True
while val:
    date = input('Enter a correct date like this DDMMYYYY\n')
    if isInt(date) and verifyDate(date):
        val = False
        print('The day of the week of', date, 'is:', whichDate(date))
    else:
        print('You entered a wrong date! Try again')