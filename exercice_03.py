def isInt(n):
    """
    This function verifies if n is an integer or not
    """
    try:
        int(n)
        return True
    except ValueError:
        return False
    
def isJanus(n):
    """
    This function verifies if an integer n is Janus or not
    """
    j = 0
    a = 0
    for i in(n):
        a = a + int(i) * (10 ** j)
        j = j + 1
    return a == int(n)

val1 = True
val2 = True
tab = []

print("You're looking for Janus numbers between a and b")
while val1:
    a = input('Enter the value of a\n')
    if isInt(a):
        val1 = False
        while val2:
            b = input('Enter the value of b\n')
            if isInt(b):
                val2 = False
                if (int(a) > int(b)):
                    print('b must be more than a! Try again')
                    val2 = True
                else:
                    for i in range(int(a), int(b)+1):
                        if isJanus(str(i)):
                            tab.append(i)
                    print("Janus numbers between", a,"and", b,"are:\n", tab)
            else:
                print(b, 'is not an integer! Try again')         
    else:
        print(a, 'is not an integer! Try again')                            