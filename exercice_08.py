def isPalindrome(sentence:str)->bool:
    """
    This function verifies if a sentence is a palindrome of not
    """
    tab = sentence.split()
    mots = ('').join(tab)
    return mots.upper() == mots[::-1].upper()

a = input('Enter a sentence\n')
print(a, 'is a palindrome' if isPalindrome(a) else 'is not a palindrome')