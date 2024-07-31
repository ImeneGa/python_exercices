def isPrimary(n):
    """
    This function verifies either an integer n is primary or not
    """
    a = n // 2
    div = []
    for i in range(1, a, 1):
        if (n % i) == 0:
            div.append(i)
    return div == [1]

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

while val:
    n = input('Enter a number\n')
    if isInt(n):
        print(n, 'is primary!' if isPrimary(int(n)) else 'is not primary!')
        val = False
    else:
        print(n, 'is not an integer! Try again')