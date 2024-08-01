import math

def isInt(n):
    """
    This function verifies if n is an integer or not
    """
    try:
        int(n)
        return True
    except ValueError:
        return False
    
def isFloat(n):
    """
    This function verifies if n is a float or not
    """
    try:
        float(n)
        return True
    except ValueError:
        return False

def sqRoot(a, p):
    """
    This function gives the square root of a with a precision of p
    """
    x = a / 2
    val = True

    while val:
        b = 1 / 2 * (x + (a / x))
        error = abs((b - x) / b)
        if error <= p:
            val = False
        x = b
    return x

val1 = True
val2 = True

print('You are calculating a square root of a using a new algorithm with a precision of p')
while val1:
    a = input('Enter the value of a\n')
    if isInt(a):
        if int(a) <= 0:
            print('We can not calculate the root square of a negative or zero number with this method! Try again')
        else:
            val1 = False
            while val2:
                p = input('Enter the value of p\n')
                if isFloat(p):
                    if float(p) <= 0:
                        print(p, 'is negative or zero while it should be positive! Try again')
                    else:
                        val2 = False
                        print(f'The root square of {a} is: {(math.sqrt(int(a))):.5f} and with the new algorithm with a precision of {p} it is: {(sqRoot(int(a),float(p))):.5f}')
                
                else:
                    print(p, 'is not a float! Try again')
    else:
        print(a, 'is not an integer! Try again')