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

def isInt(n):
    """
    This function verifies if n is an integer or not
    """
    try:
        int(n)
        return True
    except ValueError:
        return False

print("You're converting an integer n to base x, with x <= 9")
val = True
val2 = True
while val:
    n = input('Enter the value of n\n')
    if isInt(n):
        val = False
        while val2:
            x = input('Enter the value of x\n')
            if isInt(x):
                if int(x) > 9:
                    print(x,'> 9 while x should be <= 9 Try again')
                else:
                    val2 = False
                    print(n, 'in base', x, 'is', convertFrom10ToBaseX(int(n), int(x)))    
            else:
                print(x, 'is not an integer! Try again')
    else:
        print(n, 'is not an integer! Try again')