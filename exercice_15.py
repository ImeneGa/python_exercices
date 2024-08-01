def isInt(n):
    """
    This function verifies if n is an integer or not
    """
    try:
        int(n)
        return True
    except ValueError:
        return False

def gcd(a, b):
    """
    This function gives gcd(a,b) with Euclidean algorithm
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
val = True
val2 = True
while val:
    a = input('Enter the value of a\n')
    if isInt(a):
        val = False
        while val2:
            b = input('Enter the value of b\n')
            if isInt(b):
                val2 = False
                print('The Greatest Common Divisor of', a, 'and', b, 'using the Euclidean algorithm is:', gcd(int(a), int(b)))
            else:
                print(b, 'is not an integer! Try again')
    else:
        print(a, 'is not an integer! Try again') 