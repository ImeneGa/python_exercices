def missingNumber(tab):
    """
    This function looks for the unique missing integer number in an ordered list of integers
    """
    j = 0

    for i in range(tab[0], tab[len(tab)-1]+1):
        #if i+1 != tab[i]:
        #    return i+1
        if i != tab[j]:
            return i
        else:
            j = j + 1
        
tab = [1, 2, 4, 5, 6, 7]
print('The missing number in', tab, 'is', missingNumber(tab))