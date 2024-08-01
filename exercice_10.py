def isInt(n):
    """
    This function verifies if n is an integer or not
    """
    try:
        int(n)
        return True
    except ValueError:
        return False

def evenOddDigits(n):
    """
    This function returns the even and odd numbers of an integer n
    """
    even = ''
    odd = ''

    for i in str(n):
        if (int(i) % 2) == 0:
            even = even + i
        else:
            odd = odd + i
    return even, odd

val = True
while val:
    n = input('Enter the value of n\n')
    if isInt(n):
        val = False
        a, b = evenOddDigits(int(n))
        print (('The even numbers of', n, 'are', a) if a != '' else (n, 'does not have even numbers'))
        print (('The odd numbers of', n, 'are', b) if b != '' else (n, 'does not have odd numbers'))
    else:
        print(n, 'is not an integer! Try again')