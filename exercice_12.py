def mirrorMultiplication(a, b):
    """
    This function gives the mirror multiplication of a and b
    """
    tab = []
    tab2 = []

    for i in str(a):
        tab.append(i)
    for j in str(b):
        tab2.append(j)
    tab.reverse()
    tab2.reverse()
    return int(''.join(tab)) * int(''.join(tab2))

tab = []

for i in range(100, 999+1):
    for j in range(10, 99+1):
        if (i * j) == mirrorMultiplication(i, j):
            tab.append([i, j])
print('Mirror multiplications of 2 integer numbers like ABC * DE = ED * CBA are', tab)