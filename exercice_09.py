def sameDigits(a, b):
    """
    This function verifies if 2 integer numbers have the same digits
    """
    if len(str(a)) != len(str(b)):
        return False
    else:
        for i in str(a):
            if not (i in str(b)):
                return False
        return True
       
def isInt(n):
    """
    This function verifies if n is an integer or not
    """
    try:
        int(n)
        return True
    except ValueError:
        return False
    
val = True
val2 = True
while val:
    a = input('Enter the first integer a \n')
    if isInt(a):
        val = False
        while val2:
            b = input('Enter the second integer b\n')
            if isInt(b):
                val2 = False
                print(a, 'and', b, 'have' if sameDigits(int(a), int(b)) else 'do not have', 'the same digits')
            else:
                print(b, 'is not an integer! Try again')
    else:
        print(a, 'is not an integer! Try again')