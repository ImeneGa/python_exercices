def isPerfect(n):
    tab = []
    for i in range(1, n-1, 1):
        if (n % i) == 0:
            tab.append(i)
    return n == sum(tab)

def isInt(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

val = True

while val:
    n = input('Enter a number \n')
    if isInt(n):
        tab = []
        for i in range(1, int(n)):
            if isPerfect(i):
                tab.append(i)
        print('All the perfect numbers between 1 and', n, 'are :\n', tab)
        val = False
    else:
        print(n,'is not en integer! Try again')