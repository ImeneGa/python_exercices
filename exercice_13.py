def allDigits(a, b, c):
    """
    This function verifies if 3 integer of 3 digits each a, b and c contains all the digits from 1 to 9
    """ 
    i = 0
    tab1 = []
    j = 0
    tab2 = []
    k = 0
    tab3 = []
    for i in str(a):
        tab1.append(i)
    for j in str(b):
        tab2.append(j)
    for k in str(c):
        tab3.append(k)
    tab = tab1 + tab2 + tab3
    tab.sort()
    return tab == ['1', '2', '3', '4', '5', '6', '7', '8', '9']

tab = []

for i in range(100, 999+1):
    for j in range(i, 999+1):
        if (len(str(i+j)) == 3) and (allDigits(i, j, i+j)):
            tab.append([i, j, i+j])
print('The bands of 9 are:', tab)