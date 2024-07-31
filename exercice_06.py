def isInt(n):
    """
    This function verifies if n is an integer or not
    """
    try:
        int(n)
        return True
    except ValueError:
        return False
    
def oneDigit(n):
    """
    This function gives the letters nomination of a 1 digit integer number
    """
    dic = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
    
    return dic[n]

def twoDigit(n):
    """
    This function gives the letters nomination of a 2 digit integer number
    """
    dic = {10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 15:'fifteen', 18:'eighteen', 20:'twenty', 
           30:'thirty', 40:'forty', 50:'fifety', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'
           }
    if n in dic:
        return dic[n]
    else:
        if str(n)[0] == '1':
            return oneDigit(int(str(n)[1])) + 'teen'
        else:
            return oneDigit(int(str(n)[0])) + 'ty' + '-' + oneDigit(int(str(n)[1]))

def threeDigit(n):
    """
    This function gives the letters nomination of a 3 digit integer number
    """
    if str(n)[1:] == '00':
        return oneDigit(int(str(n)[0])) + ' ' + 'hundred'
    else:
        return oneDigit(int(str(n)[0])) + ' ' + 'hundred' + ' ' + twoDigit(int(str(n)[1:]))

val = True

while val:
    n = input('Chose an integer n between 0 and 999\n')
    if isInt(n):
        if (int(n) > 999):
            print('n is more than 999 Try again')
        else:
            val = False
            if len(n) == 1:
                print(n, 'is', oneDigit(int(n)))
            elif len(n) == 2:
                print(n, 'is', twoDigit(int(n)))
            else:
                print(n, 'is', threeDigit(int(n)))
    else:
        print(n, 'is not an integer! Try again')
