def isPrimary(n):
    a = n // 2
    div = []
    for i in range(1, a, 1):
        if (n % i) == 0:
            div.append(i)
    return div == [1]

n = int(input('Enter a number \n'))
print(n, ' is primary!' if isPrimary(n) else ' is not primary!')
