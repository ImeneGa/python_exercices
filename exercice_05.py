def isInt(n):
    """
    This function verifies if n is an integer or not
    """
    try:
        int(n)
        return True
    except ValueError:
        return False

def isInBaseX(n, x):
    """
    This function verifies if an integer n is in base x
    """
    for i in str(n):
        if int(i) >= x:
            return False
    return True


def convertFromXtoBase10(n, x):
    """
    This function converts an integer n in base x with x <= 10 to base 10 
    """
    tab = [] 
    for i in str(n):
        tab.append(i)
    tab.reverse()
    a = ''.join(tab)
    k = 0
    res = 0
    for j in a:
        res = res + int(j) * (x ** k)
        k = k + 1
    return res

def convertFrom10ToBaseX(n, x):
    """
    This function converts an integer n in base 10 to base x with x <= 10
    """
    tab = []
    val = True
    
    while val:
        if (n // x) == 0:
            tab.append(str(n % x))
            val = False
        else:
            tab.append(str(n % x))
            n = n // x
    tab.reverse()
    return int(''.join(tab))

def isHarshad(n, x):
    """
    This function verifies if an integer n in base x is Harshad with x <= 10
    """
    res = 0

    for i in str(n):
        res = res + int(i)

    return (convertFromXtoBase10(n, x) % res) == 0

def isHarshadInAllBases(n):
    """
    This function verifies if an integer n is Harshad in all bases x with x <= 10
    """
    val = True

    for i in range(2, 11, 1):
        if isHarshad(convertFrom10ToBaseX(n, i), i) == False:
            val = False
            break
    return val

tab = []
n2 = 1
val = True

print("You will be looking for the n first Harshad integer numbers with n >= 1")
while val:
    n = input('Enter the value of n\n')
    if isInt(n):
        if int(n) == 0:
            print("n souldn't be 0 Try again")
        else:
            val = False
            while n2 <= int(n):
                if(isHarshadInAllBases(n2)):
                    tab.append(n2)
                n2 = n2 + 1
            print(tab)
    else:
        print(n, 'is not an integer! Try again')