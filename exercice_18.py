import random
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

def isPrime(n):
    """
    This function verifies if n is a primary or not
    """
    a = n // 2
    div = []
    for i in range(1, a+1, 1):
        if (n % i) == 0:
            div.append(i)
    return div == [1]

def gcd2(a, b):
    """
    This function gives gcd(a,b) with another Euclidean algorithm
    """
    if b == 0:
        return a
    else:
        if a >= b:
            return gcd2(b, a - b)
        else:
            return gcd2(a, b-a)

def findRandomPQ(length):
    """
    This function gives a tuple p an q of an integer n with a given lenght of bits
    """
    val = True
    val2 = True

    while val:
        p = random.getrandbits(length)
        if isPrime(p):
            val = False
            while val2:
                q = random.getrandbits(length)
                if isPrime(q):
                    val2 = False
                if p == q:
                    val2 = True
    return [int(p), int(q)]

def publicPrivateKey(length):
    tab = findRandomPQ(length)
    print('The value of p and q are', tab)
    n = tab[0] * tab[1]
    euler = (tab[0]-1) * (tab[1]-1)
    val = True
    while val:
        e = random.randint(2, euler-1)
        if gcd2(int(e), euler) == 1:
            val = False
    val2 = True
    d = 1
    while (d * int(e)) % euler != 1:
        d = d + 1 # there is another method
    return [n, int(e), d]

def encrypteMessage(m, tab):
    return (m ** tab[1]) % tab[0]

def decryptMessage(c, tab):
    return (c ** tab[2]) % tab[0]

val = True
val2 = True

while val:
    lenght = input('Enter the value of the lenght of p and q\n')
    if not isInt(lenght):
        print(lenght, 'is not in integer! Try again')
    else:
        val = False
        tab2 = publicPrivateKey(int(lenght))
        print('The public and private keys are :', tab2)
        while val2:
            m = input('Enter the message (an integer) you want to engrypt\n')
            if not isInt(m):
                print(m, 'is not an integer! Try again')
            else:
                val2 = False
                c = encrypteMessage(int(m), tab2)
                print('The encrypted value of', m, 'is:', c)
                print('The decrypted value of', c,' is:', decryptMessage(c, tab2))        
