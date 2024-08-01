def properDivisors(n):
    """
    This function returns a list of the proper divisors of an integer n
    """
    tab = []
    for i in range(1, n):
        if n % i == 0:
            tab.append(i)
    return tab

def areFriends(a, b):
    """
    This function verifies if 2 integer numbers a and b are friends
    """
    return ((sum(properDivisors(a)) == b) and (sum(properDivisors(b)) == a))

tab = []

for i in range (1, 501):
    for j in range(i, 501):
        if (i != j) and (areFriends(i, j)):
            tab.append([i, j])
print('The first 500 integer friends are:', tab)
