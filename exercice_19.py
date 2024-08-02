from decimal import Decimal

def isFloat(n):
    """
    This function verifies if n is a float or not
    """
    try:
        float(n)
        return True
    except ValueError:
        return False
    

def findIndex(n, tab):
    """
    This function finds the index of n in a an ordered list with unique values, if not found return where it should be and False else the index and True
    """
    i = 0
    if n in tab:
        return [tab.index(n), True]
    else:
        while n > tab[i]:
            i = i + 1
            if i == len(tab):
                break
        return [i, False]
    

def returnCoinsAndBillets(euros):
    """
    This function gives the least number of coins and billets representing what you have in euros
    """
    tab = []
    tab1 = [5, 10, 20, 50, 100, 500]
    tab2 = [1, 2]
    tab3 = [1, 5, 10, 20, 50]
    tab4 = tab1
    n = int(euros)
    n2 = euros - n
    char = 'billets of'

    while n != 0:
        [i, found] = findIndex(n, tab4)
        if i > 0:
            if not found:
                tab.append([tab4[i-1], n // tab4[i-1]])
                print(n // tab4[i-1], char, tab4[i-1])
                n = (n % tab4[i-1])
            else:
                tab.append([tab4[i], n // tab4[i]])
                print(n // tab4[i], char, tab4[i])
                n = (n % tab4[i])
        else:
            if i == 0:
                if found:
                    tab.append([tab4[i], n // tab4[i]])
                    print(n // tab4[i], char, tab4[i])
                    n = (n % tab4[i])
                else:
                    tab4 = tab2
                    char = 'coins of'
    tab4 = tab3
    n2 = int(n2 * 100)
    while n2 != 0:
        [i, found] = findIndex(n2, tab4)
        if not found:
            tab.append([tab4[i-1] / 100, n2 // tab4[i-1]])
            print(n2 // tab4[i-1], 'coins of', tab4[i-1] / 100)
            n2 = (n2 % tab4[i-1])
        else:
            tab.append([tab4[i] / 100, n2 // tab4[i]])
            print(n2 // tab4[i], 'coins of', tab4[i] / 100)
            n2 = (n2 % tab4[i])
    return tab

val = True
while val:
    money = input('What money do you have?\n')
    if isFloat(money):
        val = False
        print('Here is the change:', returnCoinsAndBillets(float(money)))
    else:
        print(money, 'is not an integer or a float! Try again')